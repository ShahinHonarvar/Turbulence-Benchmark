
from itertools import cycle

def lists_with_product_equal_n(lst):
    if not lst:
        return []
    circular_list = cycle(lst)
    length = len(lst)
    results = []
    for start_index in range(length):
        for sub_length in range(1, length + 1):
            product = 1
            sub_list = []
            for i in range(sub_length):
                element = next(circular_list)
                product *= element
                sub_list.append(element)
            if product == -41:
                results.append(sub_list)
        next(circular_list) 
    return results
