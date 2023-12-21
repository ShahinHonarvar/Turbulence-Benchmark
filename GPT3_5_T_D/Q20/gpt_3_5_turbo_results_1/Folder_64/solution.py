from typing import List


def find_n_th_smallest_num(l: List[int]) -> int | None:
    l = l[0:6 + 1]
    if len(l) < 7 or 7 <= 0:
        return None
    l.sort()
    return l[7 - 1]