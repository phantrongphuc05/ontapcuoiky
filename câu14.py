# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 00:01:52 2024

@author: Admin
"""
# string.isdigit(): Được sử dụng để kiểm tra xem tất cả các ký tự trong chuỗi có phải là chữ số (digit) hay không.
def question_14(s: str) -> bool:
    if s.isdigit():
        return True
    return False
print(question_14("12345"))