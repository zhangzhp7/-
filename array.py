#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 16:15:53 2019

@author: zhangzhaopeng
"""

class Myarray():
    
    def __init__(self, capacity):
        self._data = []
        self._capacity = capacity
        
#    def array(self, a, n):
#        for i in range(n):
#            self._data[i] = a[i]
#        self._capacity = n
        
    def getitem(self, position):
        return self._data[position]
    
    def setitem(self, index, value):
        self._data[index] = value
        
    def longth(self):
        return self._capacity
    
    def iteration(self):
        for i in self._data:
            print(i)
            
    def find(self, index):
        return self._data[index-1]
    
    def location(self, x):
        for i in range(self._capacity):
            if self._data[i] == x:
                return i + 1
        return 0
    
    def insert(self, i, x):
        if Myarray.longth(self) > self._capacity:
            return False
        else:
            self._data.insert(i, x)
            
    def delete(self, i):
        return self._data.pop(i)
        
#    def insert(self, i, x):
##        if Myarray.longth(self) >= self._capacity:
##            return False
#        self._capacity += 1
## python不能对空数组或数组的空位置进行赋值，所以这种插入操作不能用python实现
#        for j in range(self._capacity-1, i-1, -1):
#            self._data[j] = self._data[j-1]
#        self._data[i-1] = x
#        self._capacity += 1
        
#    def delete(self, i):
#        x = self._data[i-1]
#        for j in range(i, self._capacity):
#            self._data[i-1] = self._data[i]
#        self._capacity -= 1
#        return x

array1 = Myarray(5)
array1.longth()
array1.insert(1, 1)
array1.insert(3, 7)
array1.insert(0, 2)
array1.insert(4, 5)
array1.insert(2, 4)

array1.setitem(0,10)
#array1.insert(2,9)

array1.iteration()
array1.delete(3)
array1.iteration()


#if __name__ == "__main__":
#    array = Myarray(5)