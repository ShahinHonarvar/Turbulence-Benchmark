from typing import List


def find_n_th_smallest_num(l: List[int]) -> int | None:
    l = l[46:83 + 1]
    if len(l) < 15 or 15 <= 0:
        return None
    l.sort()
    return l[15 - 1]