
from collections import deque

def lists_with_product_equal_n(lst):
    n = len(lst)
    all_products = deque(maxlen = n + 1)
    results = []

    for count in range(len(lst)):
        running_list = []
        running_product = 1
        for idx in range(count, count + n):
            val = lst[idx % n]
            running_list.append(val)
            running_product *= val
            if running_product == 40:
                results.append(list(running_list))
            while running_product > 40 and running_list:
                running_product /= running_list.pop(0)

    return results
