# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:50:47 2024

@author: Admin
"""
# string.strip():Được sử dụng để loại bỏ các ký tự trắng (hoặc ký tự khác) ở đầu và cuối chuỗi.
# separator.join(danh sách, tuple, set...): Một phương thức được sử dụng để nối các phần tử trong một iterable (danh sách, tuple, set, v.v.) thành một chuỗi.
# string.split(): Dùng để tách chuỗi 
def question_18(s: str) -> str:
    s = s.strip()
    s = " ".join(s.split())
    return s
print(question_18("   Hello   World   "))