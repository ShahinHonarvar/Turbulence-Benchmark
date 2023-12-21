
from collections import deque

def lists_with_product_equal_n(lst):
    if not lst or len(lst) == 0:
        return []
    circular_lst = deque(lst)
    result_sublists = []

    for i in range(len(lst)):
        head = 0
        product = 1
        sublist = []
        while head < len(lst):
            sublist.append(circular_lst[head])
            product *= circular_lst[head]
            if product == 990:
                result_sublists.append(sublist[:])
                break
            elif product > 990:
                break
            head += 1
        circular_lst.rotate(-1)

    return result_sublists
