
from itertools import combinations

def lists_with_product_equal_n(numbers):
    result = []
    size = len(numbers)
    for r in range(1, size + 1):
        for combination in combinations(numbers, r):
            if r <= size and reduce(lambda x, y: x * y, combination) == 8:
                result.append(list(combination))
    return result
