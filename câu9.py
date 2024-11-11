# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:35:00 2024

@author: Admin
"""
# separator.join(danh sách, tuple, set...): Một phương thức được sử dụng để nối các phần tử trong một iterable (danh sách, tuple, set, v.v.) thành một chuỗi.
# string.isalnum(): Một phương thức của đối tượng chuỗi (string) được sử dụng để kiểm tra xem tất cả các ký tự trong chuỗi có phải là chữ cái hoặc số hay không. 
def question_9(s: str) -> bool:
    chuỗi_s = ''.join(i.lower() for i in s if i.isalnum())
    chuỗi_s_đảo = chuỗi_s[::-1]
    return chuỗi_s == chuỗi_s_đảo
print(question_9("A man, a plan, a canal: Panama"))

