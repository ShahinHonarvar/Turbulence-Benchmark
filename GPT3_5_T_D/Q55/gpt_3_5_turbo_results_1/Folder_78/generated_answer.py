
from typing import List

def lists_with_product_equal_n(lst: List[int]) -> List[List[int]]:
    result = []
    length = len(lst)
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            product *= lst[j % length]
            if product == 74:
                result.append(lst[i:j % length + 1])
    return result
