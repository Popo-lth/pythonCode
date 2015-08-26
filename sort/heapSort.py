#!/usr/bin/env python
#-*- coding: utf-8 -*-
# FileName: heapSort.py
# Author: liutianhao.pro@gmail.com

import sys
import time
import random

class Solution:

    # @param {integer[]} nums
    def heapSort(self, nums):
        end = self.buildMaxHeapify(nums)

        for i in xrange(end, 0, -1):
            (nums[i], nums[0]) = (nums[0], nums[i])
            self.maxHeapify(nums, 0, i-1)

    def buildMaxHeapify(self, nums):
        end = len(nums)
        start = (end >> 1) - 1
        end -= 1

        for i in xrange(start, -1, -1):
            #print '%d: ' % i,
            self.maxHeapify(nums, i, end)
            #print nums

        return end

    def maxHeapify(self, nums, start, end):
        root = start

        while True:
            child = (root << 1) + 1
            if child > end:
                break
            if child + 1 <= end and nums[child] < nums[child+1]:
                child += 1
            if nums[root] < nums[child]:
                (nums[root], nums[child]) = (nums[child], nums[root])
                root = child
            else:
                break

    def createArray(self):
        array = []
        for i in xrange(0, random.randint(500,1000)):
            array.append(random.randint(0, 100))
        return array


if __name__ == '__main__':
    s = Solution()

    a = s.createArray()
    #a = [92, 29, 41, 84, 94, 89, 8, 99, 84, 7]
    print a
    
    aa = list(a)
    start = time.time()
    s.heapSort(aa)
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
