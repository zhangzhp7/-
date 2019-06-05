#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:55:51 2019

@author: zhangzhaopeng
"""

#顺序栈的实现
class seqstack():
    
    def __init__(self):
        # 初始化
        self.val = []
        
    def length(self):
        # 长度
        return len(self.val)
    
    def push(self, x):
        # 入栈
        self.val.append(x)
        
    def pop(self):
        # 出栈
        return self.val.pop()
        
    def gettop(self):
        return self.val[self.length()-1]
    

# test

stack = seqstack()
stack.push(2)
stack.push(3)
stack.push(5)
print(stack.length())
print(stack.pop())
print(stack.gettop())  