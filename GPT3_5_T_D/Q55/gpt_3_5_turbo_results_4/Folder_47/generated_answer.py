
import itertools

def lists_with_product_equal_n(circular_list):
    sublists = []
    size = len(circular_list)
    
    for length in range(1, size + 1):
        sublists.extend(list(itertools.combinations(circular_list, length)))
    
    result = []
    for sublist in sublists:
        if eval('*'.join(map(str, sublist))) == -94:
            result.append(list(sublist))
    
    return result
