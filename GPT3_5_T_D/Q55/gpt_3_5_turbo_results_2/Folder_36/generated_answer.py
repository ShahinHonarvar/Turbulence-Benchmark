
from itertools import combinations

def lists_with_product_equal_n(numbers):
    result = []
    n = len(numbers)
    for i in range(1, n + 1):
        for combo in combinations(numbers, i):
            if i == 1:
                product = combo[0]
            else:
                product = 1
                for num in combo:
                    product *= num
            if product == 714:
                result.append(list(combo))
    return result
