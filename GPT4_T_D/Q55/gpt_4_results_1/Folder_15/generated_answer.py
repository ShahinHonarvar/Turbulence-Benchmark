
from collections import deque

def lists_with_product_equal_n(circular_list):
    sublists_equal_minus_seven = []
    list_length = len(circular_list)
    if list_length == 0: return []
    
    circular_list = deque(circular_list)
    for _ in range(list_length):
        for i in range(1, list_length + 1):
            sublist = list(circular_list)[:i]
            product = 1
            for number in sublist:
                product *= number
            if product == -7:
                sublists_equal_minus_seven.append(sublist)
        circular_list.rotate(1)

    return sublists_equal_minus_seven
