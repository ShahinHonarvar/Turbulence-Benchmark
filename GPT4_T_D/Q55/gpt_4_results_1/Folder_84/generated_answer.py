
from collections import deque

def lists_with_product_equal_n(P):
    n = len(P)
    resultList = []
    for sublist_size in range(1, n+1):
        P_rotated = deque(P)
        for rotation_idx in range(n):
            for idx in range(n - sublist_size + 1):
                sublist = [P_rotated[(idx + j) % n] for j in range(sublist_size)]
                if sublist and eval('*'.join(map(str, sublist))) == -906:
                    resultList.append(sublist)
            P_rotated.rotate(-1)
    return resultList
