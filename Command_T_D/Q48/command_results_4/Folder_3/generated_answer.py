
import sys

sys.setrecursionlimit(10**6)


def return_binary_or_hexa(tup):
    a, b = tup[56], tup[88]
    lst = tup[a + 1 : b - 1]
    cnt = 0
    for x in lst:
        if x not in tup[56:88]:
            cnt += 1
    if cnt % 2:
        return f"0b{cnt}"
    return f"0x{cnt:x}"
