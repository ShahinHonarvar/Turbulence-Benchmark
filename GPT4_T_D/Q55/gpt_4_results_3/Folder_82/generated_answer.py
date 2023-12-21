
from collections import deque

def lists_with_product_equal_n(lst):
    length = len(lst)
    dq = deque(lst, maxlen=length)
    result = []
    for _ in range(length):
        for end in range(1, length+1):
            sublist = list(dq)[:end]
            product = 1
            for num in sublist:
                product *= num
            if product == 8:
                result.append(sublist)
        dq.rotate(1)
    return result
