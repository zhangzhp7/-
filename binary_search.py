#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 10:03:14 2019

@author: zhangzhaopeng
"""


## search
# binary search

def binary_search1(nums, target):
    '''
    二分查找的非递归实现
    '''
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + (high - low) //2
        if nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            return mid
    return -1

def binary_search2(nums, target):
    '''
    二分查找的递归实现
    '''
    def bisearch(nums, target, low, high):
        if low > high:
            return 0
        else:
            mid = low + (high - low) // 2
            if nums[mid] > target:
                return bisearch(nums, target, low, mid-1)
            elif nums[mid] < target:
                return bisearch(nums, target, mid+1, high)
            else:
                return mid
    return bisearch(nums, target, 0, len(nums)-1)

# test
binary_search1([1,2,4,1,8,5], 8)
binary_search2([1,2,4,1,8,5], 8)

