
import numpy as np
def lists_with_product_equal_n(lst):
    target = 36
    result = []
    n = len(lst)
    
    for i in range(n):
        for j in range(i+1, n+1):
            temp_lst = lst[i:j] if j <= n else lst[i:] + lst[0:j-n]
            if np.prod(temp_lst) == target:
                result.append(temp_lst)
    return result
