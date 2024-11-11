# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:29:51 2024

@author: Admin
"""
# List.append(): Thêm một phần tử vào cuối danh sách 
import random 
def question_7(n: int) -> (float, float):
    danh_sách = []
    for i in range(n):
        x = random.uniform(0, 1)
        danh_sách.append(x)
    lớn_nhất = max(danh_sách)
    nhỏ_nhất = min(danh_sách)
    return (lớn_nhất, nhỏ_nhất)
print(question_7(5))