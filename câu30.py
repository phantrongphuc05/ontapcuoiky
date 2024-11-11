# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:12:28 2024

@author: Admin
"""
# Counter(): Đếm số lần xuất hiện của các phần tử trong một danh sách hoặc chuỗi
# String.Split(kí tự hoặc chuỗi muốn phân tách, số lần tối đa mà chuỗi sẽ được tách)
from collections import Counter
from typing import Dict
def question_30(paragraph: str) -> Dict[str, int]:
    paragraph = paragraph.lower()
    số_từ = paragraph.split()
    đếm_từ = Counter(số_từ)
    return dict(đếm_từ)
paragraph = "apple orange apple banana orange"
kết_quả = question_30(paragraph)
print(kết_quả)

