
from itertools import combinations

def lists_with_product_equal_n(circular_list):
    sublists = []
    size = len(circular_list)

    for i in range(1, size + 1):
        for j in range(size):
            sublist = circular_list[j:] + circular_list[:j]
            for k in range(size - i + 1):
                product = 1
                sub = sublist[k:k + i]
                for num in sub:
                    product *= num
                if product == 632:
                    sublists.append(sub)

    return sublists
