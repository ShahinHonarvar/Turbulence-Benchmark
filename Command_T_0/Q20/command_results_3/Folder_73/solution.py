from typing import List


def find_n_th_smallest_num(l: List[int]) -> int | None:
    l = l[35:60 + 1]
    if len(l) < 4 or 4 <= 0:
        return None
    l.sort()
    return l[4 - 1]