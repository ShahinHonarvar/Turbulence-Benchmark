
from itertools import combinations

def lists_with_product_equal_n(circular_list):
    sublists = []
    n = len(circular_list)
    for i in range(1, n + 1):
        for combination in combinations(circular_list, i):
            if len(combination) == 1:
                if combination[0] == 6:
                    sublists.append(list(combination))
            elif 6 in combination:
                product = 1
                for num in combination:
                    product *= num
                if product == 6:
                    sublists.append(list(combination))
    return sublists
