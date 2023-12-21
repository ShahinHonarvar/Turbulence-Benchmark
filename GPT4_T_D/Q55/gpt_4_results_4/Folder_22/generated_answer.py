
from collections import deque
from itertools import combinations, chain

def lists_with_product_equal_n(circular_list):
    # create a double copy of the list to get all sublists
    circular_list = list(chain(circular_list, circular_list))
    res = []
    for i in range(len(circular_list)//2):
        for j in range(i+1, len(circular_list)):
            sublist = circular_list[i:j]
            prod = 1
            for num in sublist:
                prod *= num
            if prod == 4:
                res.append(sublist)
    return res
