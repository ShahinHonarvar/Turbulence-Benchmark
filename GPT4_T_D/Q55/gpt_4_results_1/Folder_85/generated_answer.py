
from collections import deque
from itertools import cycle, islice
import numpy as np

def lists_with_product_equal_n(circular_list):
    circular_list = deque(circular_list)
    n = len(circular_list)
    lists = []
    for _ in range(n):
        circular_list.rotate()
        for i in range(n):
            for j in range(i+1, n+1):
                sublist = list(islice(cycle(circular_list), i, j))
                product = np.product(sublist)
                if product == -97:
                    lists.append(sublist)
    return lists
