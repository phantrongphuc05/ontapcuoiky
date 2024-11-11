# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:06:37 2024

@author: Admin
"""
# len(object): Trả về độ dài của một đối tượng 
# list.sort(): Dùng để sắp xếp các phần tử trong danh sách theo thứ tự tăng dần
# list.sort(reverse=True): Sắp xếp các phần tử trong danh sách theo thứ tự giảm dần
# list.sort(key=len): Sắp xếp theo độ dài của chuỗi 
from typing import List
def question_29(nums: List[int]) -> float:
    nums.sort()
    n = len(nums)
    if n % 2 != 0:
        return float(nums[n // 2])
    else:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2.0
print(question_29([3, 1, 4, 5, 9, 2, 6, 8, 7]))
print(question_29([1, 3, 2]))
