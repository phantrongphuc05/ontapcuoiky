# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:27:03 2024

@author: Admin
"""

def question_4(n: int) -> bool:
    if n % 2 == 0:
        return True
    elif n % 2 != 0:
        return False
print(question_4(4))