from typing import List


def find_n_th_smallest_num(l: List[int]) -> int | None:
    l = l[11:43 + 1]
    if len(l) < 16 or 16 <= 0:
        return None
    l.sort()
    return l[16 - 1]