# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 13:18:08 2022

@author: dcsem
"""

from Tree import BinaryTree
from MyStack import Stack
import operator

def buildParseTree(exp):
    
    '''Takes an expression as an argument and returns parse tree.'''
    
    exp_list = exp_tansformer(exp)
    parents_stack = Stack()
    exp_tree = BinaryTree('')
    parents_stack.push(exp_tree)
    current_tree = exp_tree
    
    for el in exp_list:
        
        if el == '(':
            current_tree.insert_left('')
            parents_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
            
        elif el in ['+','-','/','*']:
            current_tree.set_root_val(el)
            current_tree.insert_right('')
            parents_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
            
        elif el == ')':
            current_tree = parents_stack.pop()
        
        else:
            try:
                current_tree.set_root_val(int(el))
                current_tree = parents_stack.pop()
            except:
                raise ValueError('The element "{}" not integer'.format(el))

    return exp_tree

def evaluation(exp_tree):
    
    '''Takes parse tree as an argument and returns the result.'''
    
    operators = {
        '+':operator.add,
        '-':operator.sub,
        '*':operator.mul,
        '/':operator.truediv
        
        }
    
    LeftC = exp_tree.get_left_child()
    RightC = exp_tree.get_right_child()
    
    if LeftC and RightC:
        
        fn = operators[exp_tree.get_root_val()]
        return fn(evaluation(LeftC),evaluation(RightC))
    
    else:
        return exp_tree.get_root_val()


def preorder(tree):
    
    '''Conducts a preorder tree traversal and prints the tree. Returns nothing.'''
    
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())
        
def posrorder(tree):
    
    '''Conducts a postorder tree traversal and prints the tree. Returns nothing.'''
    
    if tree:
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())
        print(tree.get_root_val())

def inorder(tree):
    
    '''Conducts an inorder tree traversal and prints the tree. Returns nothing.'''
    
    if tree:
        preorder(tree.get_left_child())
        print(tree.get_root_val())
        preorder(tree.get_right_child())
        
        
def exp_tansformer(exp):
    
    '''Takes string as and arguments and transforms it to a list. Build specifically
        because the .split() method mishandled strings if there aren't spaces
        between the elements.'''
    
    result = []
    
    for el in range(len(exp)):
        
        if exp[el] in ['(',')','+','-','/','*']:
            result.append(exp[el])

        elif exp[el-1] not in ['(',')','+','-','/','*',' '] and \
            exp[el] not in ['(',')','+','-','/','*',' ']:
                temp = str(exp[el-1]) + str(exp[el])
                result.pop()
                result.append(int(temp))
        elif exp[el] not in ['(',')','+','-','/','*',' ']:
            result.append(exp[el])
    
    return result
    
        
pt = buildParseTree("((41*8)/(62-13))")
print("The tree looks like that:")
preorder(pt)
print('The result of the expression is:', evaluation(pt))