
from collections import deque

def lists_with_product_equal_n(lst):
    if not lst:
        return []
    output = []
    len_lst = len(lst)
    for i in range(len_lst):
        for j in range(i+1, len_lst + 1):
            curr_list = lst[i:j]
            product = 1
            for x in curr_list:
                product *= x
            if product == 54:
                output.append(curr_list)
        lst.rotate(-1)
    return output
