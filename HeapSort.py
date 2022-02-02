# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 10:41:48 2022

@author: dcsem
"""

# Using the buildHeap method, write a sorting function that can sort a list
# in O(nlogn) time.

def buildHeap(the_list):
        
    idx = len(the_list)//2
    currentSize = len(the_list)
    heapList = [0] + the_list[:]
    while idx > 0:
        percDown(idx,currentSize,heapList)
        idx -= 1
    
    return heapList
        
def percDown(idx,currentSize,heapList):
        
    while (idx * 2) < currentSize:
        min_child_idx = minChild(idx,currentSize,heapList)
        if heapList[idx] > heapList[min_child_idx]:
            heapList[idx],heapList[min_child_idx] = \
                heapList[min_child_idx],heapList[idx]
        idx = min_child_idx


        
def minChild(idx,currentSize,heapList):
        
    if idx * 2 + 1 > currentSize:
        return idx * 2
    else:
        if heapList[idx*2] < heapList[idx*2+1]:
            return idx*2
        else:
            return idx*2+1

def sorting_with_build_heap(the_list):
        
    the_list = buildHeap(the_list) # first step - to create a min heap

    idx_last_item = len(the_list)-1
    
    the_list[1], the_list[idx_last_item] = the_list[idx_last_item], the_list[1]
    new_list = []
    new_list.append(the_list.pop())
    idx_last_item -=1
    
    while idx_last_item > 0:
        percDown(1,idx_last_item,the_list)
        the_list[1], the_list[idx_last_item] = the_list[idx_last_item], the_list[1]
        new_list.append(the_list.pop())
        idx_last_item -=1

        
    return new_list

# alist = [68,88,61,89,94,50,4,76,66,82]
# print('The list prior sorting:',end=' ')
# print(alist)

# print('The list after sorting:',end=' ')
# print(sorting_with_build_heap(alist))


