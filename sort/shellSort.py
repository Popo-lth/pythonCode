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

        for i in xrange(1, end):
            if nums[i] < nums[i-1]:
                n = nums[i]
                j = i - 1
                while j >= 0 and nums[j] > n:
                    nums[j+1] = nums[j]
                    j -= 1
                nums[j+1] = n

    # @param {integer[]} nums
    def shellSort(self, nums):
        end = len(nums)

        step = end >> 1
        while step > 0:
            for i in xrange(step, end, step):
                if nums[i] < nums[i-step]:
                    n = nums[i]
                    j = i - step
                    while j >= 0 and nums[j] > n:
                        nums[j+step] = nums[j]
                        j -= step
                    nums[j+step] =n
            step >>= 1

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
    s.insertSort(aa)
    end = time.time()
    #print aa, 
    print '%0.6f' % (end - start)

    ab = list(a)
    start = time.time()
    s.shellSort(ab)
    end = time.time()
    #print ab, 
    print '%0.6f' % (end - start)
    
    ac = list(a)
    start = time.time()
    ac.sort()
    end = time.time()
    #print ac,
    print '%0.6f' % (end - start)

    print ab == ac and ab == aa
