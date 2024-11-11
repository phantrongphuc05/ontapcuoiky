# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:18:46 2024

@author: Admin
"""

def question_1(n: int) -> bool:
    if n<2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
print(question_1(11))