
from itertools import cycle, islice

def lists_with_product_equal_n(lst):
    nums = cycle(lst)
    sublists = []

    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            sublist = list(islice(nums, i, j))
            if sublist:
                product = 1
                for num in sublist:
                    product *= num
                if product == -82:
                    sublists.append(sublist)
        next(nums)

    return sublists
