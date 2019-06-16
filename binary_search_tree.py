#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 12:03:23 2019

@author: zhangzhaopeng
"""

## binary search tree

class TreeNode():
    
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class binary_search_tree():
    
    def __init__(self):
        
        self.root = None
        
#    def insert(self, val):
#        
#        s = TreeNode(val)
#        if self.root == None:
#            self.root = s
#        else:
#            if s.val < self.root.val:
#                self.insert(root.left, s)
#            else:
#                self.insert(root.right, s)
        
    def insert(self, val):
        
        node = TreeNode(val)
        if self.root == None:
            self.root = node
        else:
            cur = self.root
            if val < cur.val:
                if cur.left == None:
                    cur.left = node
            else:
                if cur.right == None:
                    cur.right = node
            

#    def insert(self, value: int):
#        if not self.root:
#            self.root = TreeNode(value)
#            return
#        parent = None
#        node = self.root
#        while node:
#            parent = node
#            node = node.left if node.val > value else node.right
#        new_node = TreeNode(value)
#        if parent.val > value:
#            parent.left = new_node
#        else:
#            parent.right = new_node
                    
    def delete(self, val):
        
        node = self.root
        parent = None
        while node and node.val != val:
            parent = node
            node = node.left if node.val > val else node.right
            
        if not node:
            return 
        
        if node.left == None and node.right == None:
            parent.left = None
            
        elif node.left == None:
            parent.left = node.right
        elif node.right == None:
            parent.left = node.left
        else:
            par = node
            s = node.right
            while s.left:
                par = s
                s = s.left
            node.val = s.val
            if par == node:
                par.right = s.right
            else:
                par.left = s.right
                
    def find(self, val):
        
        node = self.root
        while node and node.val != val:
            node = node.left if node.val > val else node.right
        return node


# test

t = binary_search_tree()
t.insert(1)
t.insert(2)
t.insert(3)

t.delete(3)

t.find(1)




