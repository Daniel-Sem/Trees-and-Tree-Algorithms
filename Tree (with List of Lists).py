# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 12:17:59 2022

@author: dcsem
"""

def binary_tree(r):
    
    '''Constructs a list with a root node and two empty sublists for the children.'''
    
    return [r, [], []]

def insert_left(root, new_branch):
    
    '''Adds a left subtree to the root of a tree. If there is a left child it pushes
        it down as the left child of the node we are adding.'''
        
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1,[new_branch, [], []])
    return root

def insert_right(root, new_branch):
    
    '''Adds a right subtree to the root of a tree. If there is a right child it pushes
        it down as the right child of the node we are adding.'''
        
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root

def get_root_val(root):
    
    '''Returns the root value.'''
    
    return root[0]

def set_root_val(root, new_val):
    
    '''Sets the root value. It needs the new value.'''
    
    root[0] = new_val

def get_left_child(root):
    
    '''Returns the left child of a given root.'''
    
    return root[1]

def get_right_child(root):
    
    '''Returns the right child of a given root.'''
    
    return root[2]


# tree = binary_tree('a')

# insert_left(tree, 'b')
# insert_right(get_left_child(tree), 'd')
# insert_right(tree, 'c')
# insert_right(get_right_child(tree), 'f')
# insert_left(get_right_child(tree), 'e')

# print(tree)

