#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:55:46 2019

@author: zhangzhaopeng
"""

### 双向链表的实现

class DBNode():
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None
        

class DBlist():
    
    def __init__(self):
        self._head = None
        self.next = None
        self.pre = None
        
    def length(self):
        # 链表长度
        count = 0
        cur = self._head
        while cur != None:
            count += 1
            cur = cur.next
            
        return count
    
    def addNode(self, val):
        # 尾部追加节点
        if self._head is None:
            self._head = DBNode(val)
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            node = DBNode(val)
            cur.next = node
            node.pre = cur
        
    def itera(self):
        # 遍历链表
        p = self._head
        if p == None:
            print('当前链表无数据!')
        while p.next != None:
            print(str(p.val) + '-->' , end = '')
#            print(p.val, end= '\t')
            p = p.next
        print(str(p.val))
        
        
    def insert(self, pos, val):
        # 指定位置插入节点 （后继方向插入）
        cur = self._head
        i = 1
        while i < pos:
            cur = cur.next
            i += 1
        node = DBNode(val)
        # 4个方向
        node.next = cur.next
        cur.next = node
        node.next.pre = node
        node.pre = cur
#        node.next = p
#        node.pre = p.pre
#        p.pre.next = node
#        p.pre = node
        
    def delete(self, pos):
        #删除指定位置节点
        cur = self._head
        i = 1
        while i < pos:
            cur = cur.next
            i += 1
        cur.pre.next = cur.next
        cur.next.pre = cur.pre
        
        
        

# test
dblist = DBlist()
dblist.addNode(1)        
dblist.addNode(2)
dblist.addNode(3)                
dblist.itera()      

dblist.insert(2, 5)  
dblist.insert(3, 6)      
dblist.itera()      

dblist.delete(3)
dblist.itera()      
