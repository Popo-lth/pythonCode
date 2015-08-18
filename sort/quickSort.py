#!/usr/bin/env python
#-*- coding: utf-8 -*-
# FileName: quickSort.py
# Author: liutianhao.pro@gmail.com

import sys
import time
import random

class Solution:

    # @param {integer[]} nums
    # @param {integer} i
    # @param {integer} j
    def quickSort(self, nums, i, j):
        if j - i < 1:
            return 
        p = self.partition(nums, i, j)

        self.quickSort(nums, i, p-1)
        self.quickSort(nums, p+1, j)
    
    # @param {integer[]} nums
    # @param {integer} i
    # @param {integer} j
    # @return {integer}
    # 不使用额外空间
    def partition_t(self, nums, i, j):
        (nums[i], nums[j]) = (nums[j], nums[i])
        index = i

        for x in xrange(i, j):
            if nums[x] <= nums[j]:
                (nums[index], nums[x]) = (nums[x], nums[index])
                index += 1
        (nums[index], nums[j]) = (nums[j], nums[index])
        
        return index

    # @param {integer[]} nums
    # @param {integer} i
    # @param {integer} j
    # @return {integer}
    # 使用额外空间
    def partition(self, nums, i, j):
        pivot = nums[i]

        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] <= pivot:
                i += 1
            nums[j] = nums[i]
        nums[i] = pivot
        return i

    # @param {integer[]} nums
    def bubbleSort(self, nums):
        end = len(nums) - 1

        for i in xrange(end, 0, -1):
            for j in xrange(0, i):
                if nums[j] > nums[j+1]:
                    (nums[j], nums[j+1]) = (nums[j+1], nums[j])

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
    s.bubbleSort(ac)
    end = time.time()
    print ac, 
    print '%0.6f' % (end - start)

    ac = list(a)
    start = time.time()
    s.quickSort(ac, 0, len(ac) - 1)
    end = time.time()
    print ac, 
    print '%0.6f' % (end - start)
    
    ac = list(a)
    start = time.time()
    ac.sort()
    end = time.time()
    print ac,
    print '%0.6f' % (end - start)
