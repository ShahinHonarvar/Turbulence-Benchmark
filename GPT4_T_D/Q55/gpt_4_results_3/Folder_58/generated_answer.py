
from itertools import combinations

def lists_with_product_equal_n(lst):
    result = []
    circular_list = lst * 2

    for l in range(1, len(lst)+1):
        for i in range(len(lst)):
            sublist = circular_list[i:i+l]
            product = 1
            for item in sublist:
                product *= item
            if product == 733:
                if sublist not in result:
                    result.append(sublist)
    return result
