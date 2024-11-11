# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:59:42 2024

@author: Admin
"""
# string.startswith(): Kiểm tra xem một chuỗi có bắt đầu bằng một đoạn chuỗi con cụ thể hay không. 
def question_27(strs: list[str]) -> str:
    if not strs:
        return ""
    chuỗi = strs[0]
    for s in strs[1:]:
        while not s.startswith(chuỗi):
            chuỗi = chuỗi[:-1]
            if not chuỗi:
                return ""
    return chuỗi