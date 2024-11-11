# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 12:08:26 2024

@author: Admin
"""
# list.sort(): Dùng để sắp xếp các phần tử trong danh sách theo thứ tự tăng dần
# list.sort(reverse=True): Sắp xếp các phần tử trong danh sách theo thứ tự giảm dần
# list.sort(key=len): Sắp xếp theo độ dài của chuỗi 
def question_25(nums: list[int]) -> list[int]:
    bình_phương = [số ** 2 for số in nums]
    bình_phương.sort()
    return bình_phương 
print(question_25([-4, -1, 0, 3, 10]))  
print(question_25([-7, -3, 2, 3, 11]))  
print(question_25([0])) 
