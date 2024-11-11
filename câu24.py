# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 11:52:56 2024

@author: Admin
"""

def question_24(nums: list[int]) -> int:
    a = None
    đếm = 0
    for num in nums:
        if đếm == 0:
            a = num
            đếm = 1
        elif num == a:
            đếm += 1
        else:
            đếm -= 1
    return a
print(question_24([3, 3, 4, 2, 4, 4, 2, 4, 4]))
print(question_24([6, 5, 5]))  
print(question_24([1, 1, 1, 2, 2, 2, 1]))  
