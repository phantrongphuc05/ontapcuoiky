# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 23:34:44 2024

@author: Admin
"""

from typing import List
from typing import Tuple
def question_33(nums: List[int]) -> Tuple[int, int]:
    if len(nums) < 5:
        return None 
    # Sắp xếp để tìm phần tử lớn thứ 2
    sắp_xếp_1 = sorted(nums, reverse=True)
    phần_tử_lớn_nhất_thứ_2 = sắp_xếp_1[1]  
    # Sắp xếp để tìm phần tử nhỏ thứ 5
    sắp_xếp_2 = sorted(nums)
    phần_tử_nhỏ_nhất_thứ_5 = sắp_xếp_2[4] 
    return (phần_tử_lớn_nhất_thứ_2, phần_tử_nhỏ_nhất_thứ_5)
nums = [3, 1, 4, 5, 9, 2, 6, 8, 7]
kết_quả = question_33(nums)
print(kết_quả)  

