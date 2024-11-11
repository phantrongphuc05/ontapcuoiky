# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 00:36:48 2024

@author: Admin
"""

from collections import Counter
from typing import List
def question_31(paragraph: str, n: int) -> List[str]:
    các_từ = paragraph.split()
    đếm_từ = Counter(các_từ)
    tổng_các_từ = len(các_từ)
    result = [từ for từ, đếm in đếm_từ.items() if (đếm / tổng_các_từ) * 100 > n]
    return result
paragraph = "dog cat dog dog fish fish fish fish"
n = 30
print(question_31(paragraph, n))  
