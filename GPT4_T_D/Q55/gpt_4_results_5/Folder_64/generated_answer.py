
def lists_with_product_equal_n(circ_list):
    import numpy as np
    n = len(circ_list)
    result = []

    def sublist_product(lst):
        return np.product(lst)
    
    if(n == 0):
        return result

    for start in range(n):
        for length in range(1, n+1):
            sublist = [circ_list[(start + i)%n] for i in range(length)]
            if sublist_product(sublist) == 3:
                result.append(sublist)
    return result
