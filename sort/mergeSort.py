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

        if length == 2:
            if nums[1] < nums[0]:
                (nums[0], nums[1]) = (nums[1], nums[0])
            return nums
        if length < 2:
            return nums

        m = int(length / 2)

        left = self.mergeSort(nums[:m])
        right = self.mergeSort(nums[m:])

        return self.merge(left, right)

    def merge(self, left, right):
        nums = []
        print "left: %s" % left
        print "right: %s" % right

        while left and right:
            nums.append(left.pop() if left[-1] >= right[-1] else right.pop())
        while left:
            nums.append(left.pop())
        while right:
            nums.append(right.pop())
        nums.reverse()

        print 'nums: %s' % nums
        return nums

    def createArray(self):
        array = []
        for i in xrange(0, random.randint(5,10)):
            array.append(random.randint(0, 100))
        return array


if __name__ == '__main__':
    s = Solution()

    a = s.createArray()
    a = [0, 68, 100, 34, 20, 99, 48, 33]
    print a
    
    aa = list(a)
    start = time.time()
    aa = s.mergeSort(aa)
    end = time.time()
    print aa, 
    print '%0.6f' % (end - start)

    ac = list(a)
    start = time.time()
    ac.sort()
    end = time.time()
    print ac,
    print '%0.6f' % (end - start)

    print aa == ac
