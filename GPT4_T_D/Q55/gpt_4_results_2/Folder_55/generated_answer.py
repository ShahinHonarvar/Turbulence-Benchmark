
from itertools import cycle, islice, chain

def lists_with_product_equal_n(circular_list):
    circular_list_ext = list(islice(cycle(circular_list), len(circular_list) * 2 - 1))
    sublist_product_eq_n = []
    
    for i in range(len(circular_list)):
        for j in range(i + 1, i + len(circular_list) + 1):
            sublist = circular_list_ext[i:j]
            product = 1
            for k in sublist:
                product *= k
            if product == -6:
                sublist_product_eq_n.append(sublist)
                
    return sublist_product_eq_n
