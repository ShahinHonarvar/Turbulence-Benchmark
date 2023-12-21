from typing import List


def find_n_th_smallest_num(l: List[int]) -> int | None:
    l = l[16:71 + 1]
    if len(l) < 14 or 14 <= 0:
        return None
    l.sort()
    return l[14 - 1]