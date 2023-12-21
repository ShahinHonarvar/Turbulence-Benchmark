
from itertools import combinations

def lists_with_product_equal_n(nums):
    sublists = []
    for i in range(1, len(nums) + 1):
        for sublist in combinations(nums, i):
            if 4 in sublist and all(sublist):
                product = 1
                for num in sublist:
                    product *= num
                if product == 4:
                    sublists.append(list(sublist))
    return sublists
