
from itertools import permutations

def lists_with_product_equal_n(circular_list):
    len_list = len(circular_list)
    circular_list += circular_list
    res = []
    for start in range(len_list):
        for end in range(start+1, start+len_list+1):
            sublist = circular_list[start:end]
            product = 1
            for num in sublist:
                product *= num
            if product == -23:
                res.append(sublist)
    return res
