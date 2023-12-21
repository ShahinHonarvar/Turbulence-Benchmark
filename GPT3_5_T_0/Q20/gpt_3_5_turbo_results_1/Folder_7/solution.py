from typing import List


def find_n_th_smallest_num(l: List[int]) -> int | None:
    l = l[470:654 + 1]
    if len(l) < 9 or 9 <= 0:
        return None
    l.sort()
    return l[9 - 1]