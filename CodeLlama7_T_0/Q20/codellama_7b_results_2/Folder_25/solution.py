from typing import List


def find_n_th_smallest_num(l: List[int]) -> int | None:
    l = l[13:40 + 1]
    if len(l) < 5 or 5 <= 0:
        return None
    l.sort()
    return l[5 - 1]