# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:24:34 2024

@author: Admin
"""

def question_36(nums: list[int]) -> list[list[int]]:
    kết_quả = []
    nums.sort()  
    kết_quả.append(nums[:])  
    while True:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i == -1:
            break
        n = len(nums) - 1
        while nums[n] <= nums[i]:
            n -= 1
        nums[i], nums[n] = nums[n], nums[i]
        nums[i + 1:] = reversed(nums[i + 1:])
        kết_quả.append(nums[:])
    return kết_quả 
nums = [1, 2, 3]
s = question_36(nums)
print(s)

