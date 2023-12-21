
def lists_with_product_equal_n(circular_list):
    from collections import deque
    from operator import mul
    from itertools import islice
    from functools import reduce

    circular_list = deque(circular_list)
    length = len(circular_list)
    product_lists = []

    for i in range(length):
        for j in range(1, length + 1):
            sublist = list(islice(circular_list, 0, j))
            sublist_product = reduce(mul, sublist, 1)
            if sublist_product == -75:
                product_lists.append(sublist)
        circular_list.rotate(-1)
    return product_lists
