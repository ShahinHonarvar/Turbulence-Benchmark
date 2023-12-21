
from itertools import cycle, islice

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    circular_list = cycle(circular_list)
    result = []

    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = list(islice(circular_list, start, end))
            product = 1
            for num in sublist:
                product *= num
            if product == -10:
                result.append(sublist)
    return result
