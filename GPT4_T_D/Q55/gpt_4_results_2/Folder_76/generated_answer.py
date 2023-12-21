
from itertools import cycle, islice

def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    all_sublists = []
    
    for i in range(length):
        for j in range(i+1, length+1):
            prod = 1
            sublist = list(islice(cycle(circular_list), i, j))
            for num in sublist:
                prod *= num
            if prod == 247:
                all_sublists.append(sublist)
                
    return all_sublists
