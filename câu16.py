# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:42:52 2024

@author: Admin
"""

def question_16(*arg) -> float:
    if not arg:
        return None
    return sum(arg)/len(arg)
print(question_16(1,2,3,4,5))
print(question_16(10,20))
print(question_16())