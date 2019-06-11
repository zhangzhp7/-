#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 19:19:40 2019

@author: zhangzhaopeng
"""

## 链队列
class Node:
    
    def __init__(self, data, next = None):
        self._data = data
        self._next = next
        
class LinkedQueue:
    
    def __init__(self):
        self._head = None
        self._tail= None
        
    def enqueue(self, item):
        new_node = Node(item)
        if self._tail != None:
            self._tail._next = new_node
        else:
            self._head = new_node
        self._tail = new_node
        
    def dequeue(self):
        if self._head != None:
            value = self._head._data
            self._head = self._head._next
        return value
    
    def __print__(self):
        cur = self._head
        val = []
        while cur != None:
            val.append(cur._data)
            cur = cur._next
        return '->'.join(str(i) for i in val) 


# test
q = LinkedQueue()
for i in range(5):
    q.enqueue(i)

q.__print__()
for _ in range(3):
    q.dequeue()

q.__print__()