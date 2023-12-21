
from collections import deque

def lists_with_product_equal_n(circular_list):
    num_list = list(circular_list)
    num_list.extend(circular_list)
    target_product = 74
    results = []

    for i in range(len(circular_list)):
        for j in range(i+1, i+len(circular_list)+1):
            sublist = num_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == target_product:
                results.append(sublist)

    return results
