# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:28:11 2024

@author: Admin
"""

def question_5(lst: list, x: int) -> int or None:
    if x in lst:
        return lst.index(x)   
    return None
print(question_5([1, 2, 3, 4, 5], 3))