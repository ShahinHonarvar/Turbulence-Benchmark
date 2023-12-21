
from collections import deque
from functools import reduce
import operator

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    queue = deque(maxlen=n)
    result = []
    if not circular_list:
        return result
    for i in circular_list:
        queue.append(i)
        for j in range(1, n+1):
            if reduce(operator.mul, list(queue)[-j:]) == 415:
                result.append(list(queue)[-j:])
    return result
