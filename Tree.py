# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 13:14:16 2022

@author: dcsem
"""

class BinaryTree:
    
    '''Implementation of a Binary Tree with using nodes and references.'''
    
    def __init__(self, Obj):
        
        self.key = Obj
        self.LeftChild = None
        self.RightChild = None
        
    def insert_left(self,Obj):
        
        if self.LeftChild == None:
            self.LeftChild = BinaryTree(Obj)
            
        else:
            temp = BinaryTree(Obj)
            temp.LeftChild = self.LeftChild
            self.LeftChild = temp
            
    def insert_right(self,Obj):
        
        if self.RightChild == None:
            self.RightChild = BinaryTree(Obj)
            
        else:
            temp = BinaryTree(Obj)
            temp.RightChild = self.RightChild
            self.RightChild = temp
            
    def get_root_val(self):
        
        return self.key
    
            
    def set_root_val(self,new_val):
        
        self.key = new_val
        
    def get_left_child(self):
        
        return self.LeftChild
    
    def get_right_child(self):
        
        return self.RightChild
    
        

# tree = BinaryTree('a')
# tree.insert_left('b')

# tree.get_left_child().insert_right('d')

# tree.insert_right('c')

# tree.get_right_child().insert_left('e')
# tree.get_right_child().insert_right('f')

# print(tree.get_root_val())
# print(tree.get_left_child().get_root_val())            
# print(tree.get_right_child().get_root_val())

# print(tree.get_left_child().get_right_child().get_root_val())

# print(tree.get_right_child().get_left_child().get_root_val())            
# print(tree.get_right_child().get_right_child().get_root_val())
