# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:52:18 2024

@author: Admin
"""
from typing import Optional
def question_20() -> Optional[str]:
    s = input("Nhập giá trị từ bán phím: ")
    if s:
        return s
    else:
        return None
print(question_20())