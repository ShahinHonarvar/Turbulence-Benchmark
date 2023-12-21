from typing import List


def find_n_th_smallest_num(l: List[int]) -> int | None:
    l = l[12:90 + 1]
    if len(l) < 17 or 17 <= 0:
        return None
    l.sort()
    return l[17 - 1]