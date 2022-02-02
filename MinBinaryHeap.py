# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 15:30:13 2022

@author: dcsem
"""

class BinHeap():
    
    '''Implementation of Binary Heap with the smallest element as a root.'''
        
    def __init__(self):
        
        self.heapList  = [0]
        self.currentSize = 0
        
    def insert(self, new_item):
        
        self.heapList.append(new_item)
        self.currentSize += 1
        self.percUp(self.currentSize)
        
    def percUp(self, idx):
        
        while idx // 2 > 0:
            
            if self.heapList[idx] < self.heapList[idx // 2]:
                
                self.heapList[idx], self.heapList[idx // 2] = \
                    self.heapList[idx // 2], self.heapList[idx]
            idx = idx // 2
        
    def findMin(self):
        
        return self.heapList[1]
    
    def minChild(self, idx):
        
        if idx * 2 + 1 > self.currentSize:
            return idx * 2
        else:
            if self.heapList[idx*2] < self.heapList[idx*2+1]:
                return idx*2
            else:
                return idx*2+1
            
    
    def percDown(self, idx):
        
        while (idx * 2) < self.currentSize:
            min_child_idx = self.minChild(idx)
            if self.heapList[idx] > self.heapList[min_child_idx]:
                self.heapList[idx],self.heapList[min_child_idx] = \
                    self.heapList[min_child_idx],self.heapList[idx]
            idx = min_child_idx
    
    def delMin(self):
        
        return_item = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.heapList.pop()
        self.currentSize -= 1
        self.percDown(1)
        
        return return_item
        
    def show(self):
        
        for item in self.heapList[1:]:
            print(item)
            
    def isEmpty(self):
        
        '''Returns true if the heap is empty, false otherwise.'''
        
        if self.currentSize == 0:
            return True
        else:
            return False
    
    def size(self):
        
        '''Returns the number of items in the heap.'''
        
        return self.currentSize

    def buildHeap(self,the_list):
        
        idx = len(the_list)//2
        self.currentSize = len(the_list)
        self.heapList = [0] + the_list[:]
        while idx > 0:
            self.percDown(idx)
            idx -= 1
    
# bh = BinHeap()
# print(bh.isEmpty())
# bh.buildHeap([2,12,8,5,44,3,1])
# # bh.insert(2)
# # bh.insert(12)
# # bh.insert(8)
# # bh.insert(5)
# # bh.insert(44)
# # bh.insert(3)
# # bh.insert(1)
# print('The size is:', bh.size())
# bh.show()
# print('...')
# print(bh.findMin())
# bh.delMin()
# print(bh.findMin())
# bh.delMin()
# print('...')
# bh.show()
# print('...')
# print(bh.findMin())
# bh.delMin()
# print(bh.findMin())
# bh.delMin()
# print(bh.isEmpty())
# print('...')
# print('The size is:', bh.size())
# bh.show()

