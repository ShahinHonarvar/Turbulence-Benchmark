
from collections import deque

def lists_with_product_equal_n(circular_list):
    n = 32
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            sublist = circular_list[i:j+1]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                sublists.append(sublist)
        # rotate the circular list to create a new starting point
        circular_list = deque(circular_list)
        circular_list.rotate(1)
        circular_list = list(circular_list)
    return sublists
