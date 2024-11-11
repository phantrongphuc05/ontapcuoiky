# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 00:19:14 2024

@author: Admin
"""

def question_38(n: int) -> int:
    if n == 0:
        return 1  
    elif n == 1:
        return 1  
    bậc_thang = [0] * (n + 1)
    bậc_thang[0] = 1 
    bậc_thang[1] = 1  
    for i in range(2, n + 1):
        bậc_thang[i] = bậc_thang[i - 1] + bậc_thang[i - 2]
    return bậc_thang[n]
n = 5
print(question_38(n))  
