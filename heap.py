#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 10:24:46 2019

@author: zhangzhaopeng
"""

## 堆以及堆排序

class heap:
    
    def __init__(self, capacity):
        
        self.data = [0]*(capacity + 1)
        self.capacity = capacity
        # 记录堆当前的元素个数
        self.count = 0

    def siftup(self):
        # 堆的上滑调整
        j = self.count
        parent = self.count // 2 # j的双亲节点
        while parent > 0 and self.data[j] > self.data[parent]:
#            if self.data[parent] >= self.data[j]:  # 双亲节点大于子节点，不调整
#                break
#            else: 
#            self.data[j] = self.data[parent]
#            self.data[parent] = self.data[j]
            self.data[j], self.data[parent] = self.data[parent], self.data[j]
            j, parent = parent, parent // 2
            

    def insert(self, value):
        # 堆的插入
        if self.count >= self.capacity:
            return 
        self.count += 1
        self.data[self.count] = value
        self.siftup()
    
    @classmethod    
    def siftdown(cls, a, k, count):
        
        i = k 
        j = 2*i # i指向被筛选节点， j指向节点i的左孩子
        while j <= count: # 筛选还没有进行到叶子
            if j < count and a[j] < a[j+1]:
                j += 1 # 比较i的左右孩子，j指向较大者
            if a[i] > a[j]:
                break # 根节点已经大于左右孩子中的较大者
            else:
                a[i], a[j] = a[j], a[i]
                i = j
                j = 2*i
     
    @classmethod           
    def HeapSort(cls, a):
        
        for i in range((len(a)-1)//2, 0, -1):
            cls.siftdown(a, i, len(a)-1)
#        for i in range(1, len(a)-1-1):
#            a[0], a[len(a)-1-i] = a[len(a)-1-i], a[0]
#            cls.siftdown(a, 1, len(a)-1-i)
        k = len(a) - 1
        while k > 1:
            a[1], a[k] = a[k], a[1]
            k -= 1
            cls.siftdown(a, 1, k)    
#        return a[1:]
#            
    
        
    def __repr__(self):
        return self.data[1 : self.count + 1].__repr__()        
        


# test
h = heap(10)
h.insert(4)
h.insert(3)
h.insert(5)
h.__repr__()

a = [0, 6, 3, 4, 0, 9, 2, 7, 5, -2, 8, 1, 6, 10]
heap.HeapSort(a)
print(a)