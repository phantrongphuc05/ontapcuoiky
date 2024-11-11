# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:24:33 2024

@author: Admin
"""

def question_3(s: str) -> (int, int):
    return len([i for i in s if i.isupper()]), len([i for i in s if i.islower()])
print(question_3("Helllo World"))