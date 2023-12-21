
from itertools import cycle, islice

def lists_with_product_equal_n(lst):
    n = len(lst)
    circular_list = cycle(lst)
    output_list = []
    for start in range(n):
        for end in range(start + 1, n + 1):
            sublist = list(islice(circular_list, start, end))
            product = 1
            for num in sublist:
                product *= num
            if product == 99:
                output_list.append(sublist)
        next(circular_list)
    return output_list
