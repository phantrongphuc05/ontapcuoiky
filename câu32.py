# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 23:20:44 2024

@author: Admin
"""

from typing import List
from typing import Tuple
def question_32(nums: List[int]) -> Tuple[List[int], List[int]]:
#Số chẵn 
    số_chẵn = []
    for số in nums:
        if số % 2 == 0:
            số_chẵn.append(số)
        số_chẵn = sorted(số_chẵn, reverse=True)
#Số lẻ 
    số_lẻ = []
    for số in nums:
        if số % 2 != 0:
            số_lẻ.append(số)
        số_lẻ = sorted(số_lẻ)
    return (số_chẵn, số_lẻ)
nums = [3, 5, 7, 6, 10, 22]
kết_quả = question_32(nums)
print(kết_quả)

