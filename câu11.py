# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:39:25 2024

@author: Admin
"""

def question_11(n: int) -> int:
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
print(question_11(10))
        