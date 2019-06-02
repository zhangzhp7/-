#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 20:55:24 2019

@author: zhangzhaopeng
"""

## 单链表的实现
class Node():
    #节点的初始化
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
        
        
class SinglyLinkedList():
    
    #单链表的初始化
    def __init__(self):
        self._head = None
        
    def find_by_value(self, value):
        #按数值在单链表查找
        
        node = self._head
        while node != None and node.val != value:
            node = node.next
        else :
            return node
        
    def find_by_index(self, index):
        # 按索引查找
        
        if self._head is None:
            print('当前链表为空！')
            return None
        
        if index <= 0:
            print('index %d不合法！'%index)
        
        else:
            node = self._head
            pos = 1
            while node != None and pos != index:
                node = node.next
                pos += 1
            return node.val
        
    def Insert(self, i, x):
        #在第i个位置插入x
        p = self._head
        count = 0
        while p != None and count != i-1:
            p = p.next
            count += 1
        s = Node(x)
        s.next = p.next
        p.next = s
        
    def addNode(self, value):
        
        if self._head is None:
            self._head = Node(value, next = None)
            
        else:
            p = self._head
            while p.next != None:
                p = p.next
            p.next = Node(value, next = None)
            
    
            
            
    def itera(self):
        
        # 遍历单链表
        p = self._head
        if p == None:
            print('当前链表无数据!')
        while p.next != None:
            print(str(p.val) + '-->' , end = '')
#            print(p.val, end= '\t')
            p = p.next
        print(str(p.val))
#        print()
        
    def delete(self, i):
        
        if i == 1:
            self._head = self._head.next
        else:
            p = self._head
            count = 2
            while p != None and count < i:
                p = p.next
                count += 1
            if p == None or p.next == None:
                print('出错！')
            else:
                q = p.next
                p.next = q.next
            
            
        
## test
            
linked = SinglyLinkedList()
linked.addNode(1)
linked.addNode(2)
linked.itera()

print(linked.find_by_index(1))
print(linked.find_by_value(2))

linked.Insert(2,3)
linked.itera()

linked.delete(2)
linked.itera()







