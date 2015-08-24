#!/usr/bin/env python
#-*- coding: utf-8 -*-
# FileName: selectionSort.py
# Author: liutianhao.pro@gmail.com

import sys
import time
import random

class Solution:

    # @param {integer[]} nums
    def selectionSort(self, nums):
        end = len(nums)

        for i in xrange(0, end):
            mn = nums[i]
            index = i
            for j in xrange(i, end):
                if nums[j] < mn:
                    index = j
                    mn = nums[j]
            (nums[i], nums[index]) = (nums[index], nums[i])

    def createArray(self):
        array = []
        for i in xrange(0, random.randint(500,1000)):
            array.append(random.randint(0, 100))
        return array


if __name__ == '__main__':
    s = Solution()

    a = s.createArray()
    #a = [29, 69, 53, 31, 75, 55]
    print a
    
    aa = list(a)
    start = time.time()
    s.selectionSort(aa)
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
