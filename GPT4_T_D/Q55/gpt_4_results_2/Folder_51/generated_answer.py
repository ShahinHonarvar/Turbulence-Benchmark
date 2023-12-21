
from collections import deque
from operator import mul
from functools import reduce
from itertools import combinations

def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    sublists = []
    for i in range(size):
        circular_list = deque(circular_list)
        circular_list.rotate(i)
        for n in range(1, len(circular_list) + 1):
            for seq in combinations(circular_list, n):
                if reduce(mul, seq) == -44:
                    sublists.append(list(seq))
    return sublists
