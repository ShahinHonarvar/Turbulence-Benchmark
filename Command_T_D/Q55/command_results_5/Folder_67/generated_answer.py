import itertools
def lists_with_product_equal_n(nums):
    result = []
    for p in itertools.permutations(nums, 2):
        prod = 1
        for i in range(1, len(p)):
            prod *= p[i]
        if prod == 33:
            result.append(list(p))
    return result
