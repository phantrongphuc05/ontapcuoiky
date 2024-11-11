# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:42:06 2024

@author: Admin
"""

#split là tách chuỗi 
def question_13(s: str) -> int:
    các_từ = s.split()
    return len(các_từ)
print(question_13("Hello world, how are you?"))