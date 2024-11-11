# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:41:29 2024

@author: Admin
"""

def question_12() -> bool:
    import random
    n = random.randint(1, 1000)
    print(f"Số ngẫu nhiên là: {n}")
    if n<2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
        return True
print(question_12())