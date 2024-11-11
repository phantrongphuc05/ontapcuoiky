# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:55:52 2024

@author: Admin
"""

def question_22(nums: list[int]) -> None:
    i = 0  
    for số in nums:
        if số != 0:
            nums[i] = số
            i += 1
    while i < len(nums):
        nums[i] = 0
        i += 1
nums = [0, 1, 0, 3, 12]
question_22(nums)
print(nums) 