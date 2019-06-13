#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 12:22:43 2019

@author: zhangzhaopeng
"""

## 二叉树的前序、中序和后序遍历

class Node():
    
    def __init__(self, val = -1, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class Tree():
    
    def __init__(self):
        self.root = Node()
        self.items = []
        
    def add(self, item):
        '''
        添加节点
        '''
        node = Node(item)
        if self.root.val == -1:
            self.root = node
            self.items.append(self.root)
            
        else:
            treeNode = self.items[0]
            if treeNode.left == None:
                treeNode.left = node
                self.items.append(treeNode.left)
                
            else:
                treeNode.right = node
                self.items.append(treeNode.right)
                # 如果该节点存在右子树， 将其丢弃
                self.items.pop(0)
                
    def pre_order(self, root):
        '''
        递归实现前序遍历
        '''
        if root:
            print(root.val)
            self.pre_order(root.left)
            self.pre_order(root.right)
            
    def in_order(self, root):
        '''
        递归实现中序遍历
        '''
        if root:
            self.in_order(root.left)
            print(root.val)
            self.in_order(root.right)
            
    def post_order(self, root):
        '''
        递归实现后序遍历
        '''
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.val)
        

# test

elems = range(10)
tree = Tree()
tree.add(1)
for i in elems:
    tree.add(i)

tree.pre_order(tree.root)
tree.in_order(tree.root)
tree.post_order(tree.root)