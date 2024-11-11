# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 23:39:42 2024

@author: Admin
"""

def question_39(prices: list[int]) -> int:
    if not prices or len(prices) < 2:
        return 0 
    giá_ban_đầu = prices[0]  
    lợi_nhuận = 0  
    for giá in prices[1:]:
        lợi_nhuận = max(lợi_nhuận, giá - giá_ban_đầu)
        giá_ban_đầu = min(giá_ban_đầu, giá)
    return lợi_nhuận
prices =  [7, 6, 4, 3, 1]
print(question_39(prices)) 