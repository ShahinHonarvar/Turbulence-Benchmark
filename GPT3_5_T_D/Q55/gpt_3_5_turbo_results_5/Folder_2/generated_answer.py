
from itertools import combinations

def lists_with_product_equal_n(circular_list):
    sublist_size = 1
    result = []
    
    while sublist_size <= len(circular_list):
        for i in range(len(circular_list)):
            sublists = [circular_list[j:j+sublist_size] for j in range(i, i+len(circular_list))]
            for sublist in sublists:
                if sublist in result:
                    continue
                if sum(sublist) == -968:
                    result.append(sublist)
        sublist_size += 1

    return result
