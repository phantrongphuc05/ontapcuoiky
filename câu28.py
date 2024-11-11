# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 13:19:03 2024

@author: Admin
"""
from typing import Dict 
def question_28(s: str) -> Dict[str, int]:
    chuỗi = {}
    for kí_tự in s:
        if kí_tự in chuỗi:
            chuỗi[kí_tự] += 1
        else:
            chuỗi[kí_tự] = 1   
    return chuỗi
print(question_28("aabbcc"))