#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:21:13 2019

@author: zhangzhaopeng
"""

## 数组实现队列

class ArrayQueue:
    # 初始化
    def __init__(self, capacity):
        self._head = 0
        self._tail = 0
        self._capacity = capacity
        self._items = []
        
    # 进队
    def enqueue(self, item):
        if self._tail == self._capacity:
            # 队列满
            if self._head == 0:
                return False
            # 队列假溢出
            else:
                for i in range(0, self._tail - self._head):
                    self._items[i] = self._items[i + self._head]
                self._tail = self._tail - self._head
                self._head = 0
        self._items.insert(self._tail, item)
        self._tail += 1
        return True
    
    # 出队
    def dequeue(self):
        if self._tail != self._head:
            item = self._items[self._head]
            self._head += 1
            return item
        else:
            return False
        
    # 打印队列
    def __print__(self):
        return " ".join([str(item) for item in self._items[self._head:self._tail]])
    
# test
q = ArrayQueue(2)
q.enqueue(1)    
q.enqueue(2)    

q.__print__()    
q.dequeue()    
q.__print__()    
    
    
    
    
    
    
    
    
    
    
        