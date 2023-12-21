
from collections import deque

def lists_with_product_equal_n(circular_list):
    def get_sublists(lst):
        for sublist_length in range(1, len(lst) + 1):
            for i in range(len(lst)):
                yield lst[i:i+sublist_length]

    circular_list = list(deque(circular_list, len(circular_list)))
    sublists = list(get_sublists(circular_list))
    result = []

    for sublist in sublists:
        if len(sublist) <= len(circular_list) and len(sublist) != 0:
            product = 1
            for number in sublist:
                product *= number
            if product == 632:
                result.append(sublist)

    return result
