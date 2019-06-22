#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 20:51:36 2019

@author: zhangzhaopeng
"""

## 散列表实现：开散列表

num = 10


# 一个数据节点
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class HashTable(object):
    def __init__(self):
        self.value = [None] * num

    def insert(self, data):
        if self.search(data):
            return True

        i = data % num
        node = Node(data)
        if self.value[i] is None:
            self.value[i] = node
            return True
        else:
            head = self.value[i]
            while head.next is not None:
                head = head.next
            head.next = node
            return True

    def search(self, data):
        i = data % num
        if self.value[i] is None:
            return False
        else:
            head = self.value[i]
            while head and not head.data == data:
                head = head.next
            if head:
                return head
            else:
                return False

    def delete(self, data):
        if self.search(data):
            i = data % num
            if self.value[i].data == data:
                self.value[i] = self.value[i].next
            else:
                head = self.value[i]
                while not head.next.data == data:
                    head = head.get_next()
                head.next = head.next.next
            return True
        else:
            return False

    def echo(self):
        i = 0
        for head in self.value:
            print(str(i) + ':\t')
            if head is None:
                print(None),
            else:
                while head is not None:
                    print(str(head.data) + ' ->')
                    head = head.next
                print(None),
            print('')
            i += 1
        print('')


if __name__ == '__main__':
    hashTable = HashTable()
    hashTable.insert(10)
    hashTable.insert(11)
    hashTable.insert(1)
    hashTable.echo()
    hashTable.delete(1)
    hashTable.echo()
