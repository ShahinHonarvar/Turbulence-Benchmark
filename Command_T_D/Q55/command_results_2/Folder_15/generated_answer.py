import itertools
def lists_with_product_equal_n(nums):
    sublists = []
    for s in itertools.permutations(nums):
        prod = 1
        for i in range(len(s)):
            prod *= s[i]
        if prod == -7:
            sublists.append(s)
    return sublists
