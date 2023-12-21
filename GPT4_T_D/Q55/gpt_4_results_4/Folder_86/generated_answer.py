
import numpy as np

def lists_with_product_equal_n(circle):
    target = -779
    n = len(circle)
    
    circle = circle * 2
    
    all_lists = []
    for i in range(n):
        product = circle[i]
        k = i + 1
        if product == target:
            all_lists.append(circle[i:k])
        while product != target and k < i + n:
            product *= circle[k]
            if product == target:
                all_lists.append([circle[j] for j in range(i, k+1)])
            k += 1
    return all_lists
