from typing import List


def find_n_th_smallest_num(l: List[int]) -> int | None:
    l = l[299:635 + 1]
    if len(l) < 12 or 12 <= 0:
        return None
    l.sort()
    return l[12 - 1]