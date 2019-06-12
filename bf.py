#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 08:37:25 2019

@author: zhangzhaopeng
"""

## bf
def bf(main, pattern):
    '''
    字符串匹配，暴力搜索
    main:主串
    pattern:模式串
    查找模式串在主串的位置
    '''
    n = len(main)
    m = len(pattern)
    i, j = 0, 0
    while i < n and j < m:
        if main[i] == pattern[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
    if j == m:
        return i - j
    else:
        return -1

# test    
main = 'BBC ABCDAB ABCDABCDABDE '
pattern = 'ABCDABD'
bf(main, pattern)  