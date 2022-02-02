# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 10:25:15 2022

@author: dcsem
"""
# Create a binary heap with a limited heap size. In other words, the heap only
# keeps track of the n most important items. If the heap grows in size to more
# than n items the least important item is dropped.


class BinHeap():
    
    def __init__(self, limit):
        
        self.heapList  = [0]
        self.currentSize = 0
        self.maxSize = int(limit)
        
    def insert(self, new_item):
        
        self.heapList.append(new_item)
        self.currentSize += 1
        self.percUp(self.currentSize)
        if self.currentSize > self.maxSize:
            while self.currentSize > self.maxSize:
                self.heapList.pop()
                self.currentSize -= 1
        
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
    
# bh = BinHeap(7)
# print(bh.isEmpty())
# bh.insert(4)
# bh.insert(12)
# bh.insert(8)
# bh.insert(5)
# bh.insert(44)
# bh.insert(3)
# bh.insert(1)
# bh.insert(2)
# bh.insert(3)
# print('The size is:', bh.size())
# bh.show()

