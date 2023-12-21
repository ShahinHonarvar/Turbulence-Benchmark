
from collections import deque

def lists_with_product_equal_n(circular_list):
    product_lists = []
    circular_list = deque(circular_list)
    for _ in range(len(circular_list)):
        for i in range(1, len(circular_list)+1):
            sublist = list(circular_list)[0:i]
            product = 1
            for num in sublist:
                product *= num
            if product == 47:
                product_lists.append(sublist)
        circular_list.rotate(1)
    return product_lists
