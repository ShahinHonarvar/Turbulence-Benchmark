
from itertools import combinations

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    sublists = []
    for r in range(1, n+1):
        for start in range(n):
            indexes = [(start+i)%n for i in range(r)]
            sublist = [circular_list[i] for i in indexes]
            product = 1
            for i in sublist:
                product *= i
            if product == 13:
                sublists.append(sublist)
    return sublists
