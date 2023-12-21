
from collections import deque

def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    q = deque(circular_list)

    for _ in range(n):
        running_product = 1
        sublist = []
        for num in q:
            running_product *= num
            sublist.append(num)
            if running_product == 990:
                result.append(sublist[:])
            while sublist and running_product > 990:
                running_product //= sublist.pop(0)
        q.rotate(-1)
    return result
