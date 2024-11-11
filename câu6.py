# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:29:10 2024

@author: Admin
"""

def question_6(n: int) -> int:
    if n==0 or n==1:
        return 1
    else:
        kết_quả = n
        for i in range(2,n):
            kết_quả *= i
    return kết_quả
print(question_6(5))    