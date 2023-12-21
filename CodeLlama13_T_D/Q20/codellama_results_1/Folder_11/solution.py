from typing import List


def find_n_th_smallest_num(l: List[int]) -> int | None:
    l = l[54:87 + 1]
    if len(l) < 13 or 13 <= 0:
        return None
    l.sort()
    return l[13 - 1]