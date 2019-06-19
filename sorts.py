#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 20:05:10 2019

@author: zhangzhaopeng
"""

## 直接插入排序

def InsertSort(r):
    
    length = len(r)
    if length <= 1:
        return 
    
    for i in range(1, length):
        value = r[i]
        j = i - 1
        while j >= 0 and r[j] > value:
            r[j + 1] = r[j]
            j -= 1
        r[j + 1] = value

## 快速排序

def QuickSort(r):
    
    less = []
    more = []
    pivotlist = []
    if len(r) <= 1:
        return r
    else:
        pivot = r[0]
        for i in r:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotlist.append(i)
        less = QuickSort(less)
        more = QuickSort(more)
        return less + pivotlist + more
    

## 冒泡排序
def BubbleSort(r):
    
    length = len(r)
    if length <= 1:
        return 
    for i in range(length):
        exchange = False
        for j in range(length-i-1):
            if r[j] > r[j+1]:
                r[j], r[j+1] = r[j+1], r[j]
                exchange = True
                
## 选择排序
def SelectSort(r):
    
    length = len(r)
    if length <= 1:
        return 
    for i in range(length):
        min_index = i
        min_val = r[i]
        for j in range(i, length):
            if r[j] < min_val:
                min_val = r[j]
                min_index = j
        r[i], r[min_index] = r[min_index], r[i]
        

## test
nums = [1,3,2,5,3,9,6]
InsertSort(nums)
print(nums)

nums2 = [1,3,2,5,3,9,6]
QuickSort(nums2)

nums3 = [1,3,2,5,3,9,6]
BubbleSort(nums3)
print(nums3)

nums4 = [1,3,2,5,3,9,6]
SelectSort(nums4)
print(nums4)






