
from itertools import combinations

def lists_with_product_equal_n(n):
    sublists = []
    length = len(n)
    
    for i in range(1, length + 1):
        for j in range(length):
            sublist = n[j:j+i]
            if len(sublist) == i and n[j-1]*n[(j+i)%length] == 33:
                sublists.append(sublist)
    
    return sublists
