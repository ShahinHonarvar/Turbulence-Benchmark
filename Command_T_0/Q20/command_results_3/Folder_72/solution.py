from typing import List


def find_n_th_smallest_num(l: List[int]) -> int | None:
    l = l[21:69 + 1]
    if len(l) < 10 or 10 <= 0:
        return None
    l.sort()
    return l[10 - 1]