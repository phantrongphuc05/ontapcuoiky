# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:38:25 2024

@author: Admin
"""
# split là tách chuỗi 
def question_10() -> None:
    danh_sách = input("Nhập vào danh sách số nguyên: ")
    if not danh_sách:
        return None
    danh_sách_số_nguyên = [int(i) for i in danh_sách.split()]
    return danh_sách_số_nguyên
print(question_10())