
from collections import deque

def lists_with_product_equal_n(circular_list):
    n = 36
    results = []
    for i in range(len(circular_list)):
        sublists = []
        product = 1
        for j in range(i, len(circular_list)+i):
            if product * circular_list[j%len(circular_list)] > n:
                break
            product *= circular_list[j%len(circular_list)]
            sublists.append(circular_list[j%len(circular_list)])
            if product == n:
                results.append(sublists[:])
    return results
