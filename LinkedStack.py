#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:32:43 2019

@author: zhangzhaopeng
"""

## 链栈的实现

class Node():
    #节点类
    def __init__(self, val):
        self.val = val
        self.next = None
        
    
class LinkedStack():
    
    def __init__(self):
        self.top: Node = None
        
    def push(self, val):
        # 进栈
        new_top = Node(val)
        new_top.next = self.top
        self.top = new_top
        
    def pop(self):
        # 出栈
        if self.top != None:
            value = self.top.val
            self.top = self.top.next
        return value
    
    def itera(self):
        # 遍历栈
        cur = self.top
        nums = []
        while cur != None:
            value = cur.val
            nums.append(value)
            cur = cur.next
            
        return ' '.join(f'{num}' for num in nums)
            
        
# test
        
stack = LinkedStack()
stack.push(1)
stack.itera()
stack.pop()
stack.itera()