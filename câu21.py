# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:53:18 2024

@author: Admin
"""

def question_21(nums: list[int], target: int):
    x = {}
    for số in nums:
        y = target - số
        if y in x:
            return (y, số)
        x[số] = True
    return None
print(question_21([2, 7, 11, 15], 9)) 
print(question_21([1, 2, 3, 4, 5], 10))
