from typing import List


def find_n_th_smallest_num(l: List[int]) -> int | None:
    l = l[43:80 + 1]
    if len(l) < 6 or 6 <= 0:
        return None
    l.sort()
    return l[6 - 1]