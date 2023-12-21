
from itertools import combinations

def lists_with_product_equal_n(n=10):
    size = len(n)
    sublists = []
    for length in range(1, size + 1):
        for i in range(size):
            sublist = [n[(i+j)%size] for j in range(length)]
            if eval('*'.join(str(x) for x in sublist)) == -46:
                sublists.append(sublist)
    return sublists
