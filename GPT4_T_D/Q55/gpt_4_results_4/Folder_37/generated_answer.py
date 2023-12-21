
from itertools import cycle

def lists_with_product_equal_n(lst):
    result = []
    for start_idx in range(len(lst)):
        multipliers = cycle(lst)
        for _ in range(start_idx):
            next(multipliers)
        product = 1
        sublist = []
        for num in multipliers:
            if abs(product*num) >= abs(76) and product*num != 76:
                break
            product *= num
            sublist.append(num)
            if product == -76:
                result.append(list(sublist))
                break
    return result
