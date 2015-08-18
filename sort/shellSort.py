#!/usr/bin/env python
#-*- coding: utf-8 -*-
# FileName: shellSort.py
# Author: liutianhao.pro@gmail.com

import sys
import time
import random

class Solution:

    # @param {integer[]} nums
    def insertSort(self, nums):
        end = len(nums)

        for i in xrange(end, 0, -1):
            for 


    # @param {integer[]} nums
    def shellSort(self, nums):
        print 'shellSort'

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
    
    ac = list(a)
    start = time.time()
    s.insertSort(ac)
    end = time.time()
    print ac, 
    print '%0.6f' % (end - start)

    ac = list(a)
    start = time.time()
    s.shellSort(ac)
    end = time.time()
    print ac, 
    print '%0.6f' % (end - start)
    
    ac = list(a)
    start = time.time()
    ac.sort()
    end = time.time()
    print ac,
    print '%0.6f' % (end - start)
