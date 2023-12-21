from typing import List


def find_n_th_smallest_num(l: List[int]) -> int | None:
    l = l[0:17 + 1]
    if len(l) < 18 or 18 <= 0:
        return None
    l.sort()
    return l[18 - 1]