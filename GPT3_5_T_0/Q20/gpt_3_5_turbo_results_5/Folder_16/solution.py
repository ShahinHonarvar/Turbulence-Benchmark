from typing import List


def find_n_th_smallest_num(l: List[int]) -> int | None:
    l = l[35:83 + 1]
    if len(l) < 8 or 8 <= 0:
        return None
    l.sort()
    return l[8 - 1]