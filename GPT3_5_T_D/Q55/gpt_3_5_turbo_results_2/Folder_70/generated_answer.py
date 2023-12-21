
from itertools import combinations

def lists_with_product_equal_n(lst):
    result = []
    for i in range(1, len(lst) + 1):
        for j in range(len(lst)):
            sublists = list(combinations(lst, i))
            for sublist in sublists:
                if len(sublist) == len(lst):
                    sublist += sublist[:-1]
                
                product = 1
                for num in sublist:
                    product *= num
                    
                if product == 32:
                    result.append(list(sublist))
    return result
