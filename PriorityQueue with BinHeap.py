# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 15:15:05 2022

@author: dcsem
"""

# Using the BinaryHeap class, implement a new class called PriorityQueue. Your
# PriorityQueue class should implement the constructor, plus the enqueue and
# dequeue methods.

class BinHeap():
    
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
            
class PriorityQueue:
    
    '''PriorityQueue implementation using Binary Heap as underlying data structure.'''
    
    def __init__(self):
    
        self.pqueue = BinHeap()
    
    def enqueue(self,new_item):
        
        self.pqueue.insert(new_item)
    
    def dequeue(self):
        
        self.pqueue.delMin()
        
    def show(self):
        
        self.pqueue.show()
        
   
    
    