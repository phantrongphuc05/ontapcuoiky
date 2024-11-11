# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:57:50 2024

@author: Admin
"""
#set: loại bỏ các phần tử trùng lặp trong mảng nums 
def question_23(nums: list[int]) -> bool:
    s = set()  
    for n in nums:
        if n in s: 
            return True  
        s.add(n)    
    return False  
print(question_23([1, 2, 3, 1]))  
print(question_23([1, 2, 3, 4])) 
print(question_23([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
