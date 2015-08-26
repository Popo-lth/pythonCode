#!/usr/bin/env python
#-*- coding: utf-8 -*-
# FileName: mergeSort.py
# Author: liutianhao.pro@gmail.com

import sys
import time
import random

class Solution:

    # @param {integer[]} nums
    def mergeSort(self, nums):
        length = len(nums)

        if length == 1:
            if nums[1] < nums[0]:
                (nums[0], nums[1]) = (nums[1], nums[0])
        elif length == 0:
            return nums

        

        print 'mergeSort'

    def merge(self, lst1, lst2):
        return []

    def createArray(self):
        array = []
        for i in xrange(0, random.randint(5,10)):
            array.append(random.randint(0, 100))
        return array


if __name__ == '__main__':
    s = Solution()

    a = s.createArray()
    #a = [29, 69, 53, 31, 75, 55]
    print a
    
    aa = list(a)
    start = time.time()
    s.mergeSort(aa)
    end = time.time()
    #print aa, 
    print '%0.6f' % (end - start)

    ac = list(a)
    start = time.time()
    ac.sort()
    end = time.time()
    #print ac,
    print '%0.6f' % (end - start)

    print aa == ac
