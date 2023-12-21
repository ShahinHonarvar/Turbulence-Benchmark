
from collections import deque

def lists_with_product_equal_n(lst):
    length = len(lst)
    circular_list = deque(lst)
    result = []
    for _ in range(len(lst)):
        for end in range(2, length+1):
            start = 0
            while start < end:
                sublist = list(circular_list)[start:end]
                product = 1
                for i in sublist:
                    product *= i
                if product == 42:
                    result.append(sublist)
                start += 1
        circular_list.rotate(1)
    return result
