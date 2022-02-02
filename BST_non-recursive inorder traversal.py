# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 13:44:49 2022

@author: dcsem
"""

# Using the findSuccessor method, write a non-recursive inorder traversal for a
# binary search tree.


class TreeNode:
    
    '''CLass, that represents a singe node in a binary search tree. It need a key and
    a value. Parent, left child and right child are optinal parameters.'''
    
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        
        '''Returns True if the node has a left child and False otherwise.'''
        
        return self.leftChild

    def hasRightChild(self):
        
        '''Returns True if the node has a right child and False otherwise.'''
        
        return self.rightChild

    def isLeftChild(self):
        
        '''Returns True if the node has a parent node and it is its left child
            and False otherwise.'''
            
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        
        '''Returns True if the node has a parent node and it is its right child
            and False otherwise.'''
            
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        
        '''Returns True if the node is the root node and have no parent node
            and False otherwise.'''
            
        return not self.parent

    def isLeaf(self):
        
        '''Returns True if the node is a leaf root node and have no childern
            and False otherwise.'''
            
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        
        '''Returns True if the node has atleast one children node and False otherwise.'''
        
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        
        '''Returns True if the node has exactly two children nodes and False otherwise.'''
        
        return self.rightChild and self.leftChild

    def spliceOut(self):
        
        '''Returns nothing. Modifies the BinarySearchTree by splacing the parent and
            the children of the current node, if any.'''
            
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findSuccessor(self):
        
        '''Returns the successor. Searches the BinarySearchTree for a node to replace the
            the current node.'''
            
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                   if self.isLeftChild():
                       succ = self.parent
                   else:
                       self.parent.rightChild = None
                       succ = self.parent.findSuccessor()
                       self.parent.rightChild = self
        return succ

    def findMin(self):
        
        '''Returns the node with the minimum kay value.'''
        
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def replaceNodeData(self,key,value,lc,rc):
        
        '''Returns nothing. Modifies the node with the given key, value. left and
            right child.'''
            
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinarySearchTree:
    
    '''CLass, that represents the binary search tree(BST). It need nothing to be initialised.
        It is constructed if objects from the TreeNode class.
        
        Time complexcity of O(log2n), but can deteriorate to O(n) if the keys are sorted.'''
        
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        
        '''Returns the length of the BST.'''
        
        return self.size

    def __len__(self):
        return self.size

    def put(self,key,val):
        
        '''Modifies the BST. Need a key and a value as input. Checks if the BST has
            a root and adds a TreeNode object as a root. Else it calls the _put
            method'''
            
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        
        '''Modifies the BST. Needs a key and a value and the root node as input.
            Checks if the given key is smaller or larger than the key of the
            current node and recursevly calls itself accordingly.
            If the key exsists, the old value is replaced by the new one'''
            
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                   self._put(key,val,currentNode.leftChild)
            else:
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)
                   
        elif key == currentNode.key: # if key is duplicate, replace the old value with the new one
            currentNode.payload = val
        
        else:
            if currentNode.hasRightChild():
                   self._put(key,val,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    def __setitem__(self,k,v):
       self.put(k,v)

    def get(self,key):
        
        '''Returns a value by given key.'''
        
        if self.root:
           res = self._get(key,self.root)
           if res:
                  return res.payload
           else:
                  return None
        else:
           return None

    def _get(self,key,currentNode):
        
        '''Returns a TreeNode object by given key. Checks if the key matches the
            key of the current node and returns it. If not, calls itself with the
            left child if the right child of the current node depending on the
            value of the key.'''
        
        if not currentNode:
           return None
        elif currentNode.key == key:
           return currentNode
        elif key < currentNode.key:
           return self._get(key,currentNode.leftChild)
        else:
           return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
       return self.get(key)

    def __contains__(self,key):
        
        '''Returns a boolean by given key. True if the key is in the BST, False
            otherwise.'''
            
        if self._get(key,self.root):
           return True
        else:
           return False

    def delete(self,key):
        
        '''Modifies the BST. Checks if the tree contains given key and calls the
            remove metod if found. Raises KeyError if not found.'''
            
        if self.size > 1:
         nodeToRemove = self._get(key,self.root)
         if nodeToRemove:
             self.remove(nodeToRemove)
             self.size = self.size-1
         else:
             raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
         self.root = None
         self.size = self.size - 1
        else:
         raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
       self.delete(key)

    def remove(self,currentNode):
        
         '''Modifies the BST. Checks the position of the current node and changes
            the parent nad child pointer accordingly, if any.'''
            
         if currentNode.isLeaf(): #leaf, no children to be modified
           if currentNode == currentNode.parent.leftChild:
               currentNode.parent.leftChild = None
           else:
               currentNode.parent.rightChild = None
        
         elif currentNode.hasBothChildren(): #interior, have to find succ and move it
           succ = currentNode.findSuccessor()
           succ.spliceOut()
           currentNode.key = succ.key
           currentNode.payload = succ.payload

         else: # this node has one child, both parent and child pointers need adjustment
           if currentNode.hasLeftChild():
             if currentNode.isLeftChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.leftChild
             elif currentNode.isRightChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.leftChild
             else:
                 currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.payload,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
           else:
             if currentNode.isLeftChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.rightChild
             elif currentNode.isRightChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.rightChild
             else:
                 currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)
                 


    def inOrder_with_succ(self):
        
        current = self.root
        visited = []
        
        while current != None:
            if current.hasLeftChild() and current.leftChild not in visited:
                visited.append(current.leftChild)
                current = current.leftChild
                
            if current.hasLeftChild() and current.leftChild in visited:
                print(current.payload)
                current = current.rightChild
                
            elif current.hasRightChild():
                print(current.payload)
                current = current.rightChild
            
            elif not current.hasAnyChildren():
                print(current.payload)                
                current = current.findSuccessor()
                
            elif visited != []:
                el = visited.pop()
                print(el.payload)
                
            else:
                break

        

mytree = BinarySearchTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"

print('The element with key 6 is:',mytree[6])
print('The element with key 2 is:',mytree[2])

mytree.inOrder_with_succ()
