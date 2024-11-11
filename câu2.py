# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:19:39 2024

@author: Admin
"""
# List.append(): Thêm một phần tử vào cuối danh sách 
import random 
def question_2(n: int) -> (int, float):
    danh_sách = []
    for i in range(n):
        x = random.randint(1, 100)
        danh_sách.append(x)
    tổng = sum(danh_sách)
    trung_bình = tổng / n
    return (tổng, trung_bình)
print(question_2(5))