# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 01:06:12 2024

@author: Admin
"""
# s.find(chuỗi_con, bắt_đầu, kết_thúc): Được dùng để tìm vị trí của một chuỗi con trong chuỗi chính
# chuỗi_con = s[i:i+độ_dài] : Câu lệnh này có nghĩa là cú pháp để cắt một phần con từ chuỗi s, bắt đầu từ chỉ số i và kéo dài đến một khoảng bằng i + độ_dài 
def question_35(s: str) -> str:
    n = len(s)
    chuỗi_con_dài_nhất = ""
    for độ_dài in range(1, n // 2 + 1):
        for i in range(n - độ_dài + 1):
            chuỗi_con = s[i:i+độ_dài]
            count = 0
            start = 0
            while start < n:
                start = s.find(chuỗi_con, start)
                if start == -1: 
                    break
                count += 1
                start += độ_dài 
            if count >= 2 and độ_dài > len(chuỗi_con_dài_nhất):
                chuỗi_con_dài_nhất = chuỗi_con 
    return chuỗi_con_dài_nhất 
s = "abcabcabc"
kết_quả = question_35(s)
print(kết_quả)  

