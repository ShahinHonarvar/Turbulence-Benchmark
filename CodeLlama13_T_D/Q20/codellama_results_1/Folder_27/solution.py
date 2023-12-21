from typing import List


def find_n_th_smallest_num(l: List[int]) -> int | None:
    l = l[75:91 + 1]
    if len(l) < 11 or 11 <= 0:
        return None
    l.sort()
    return l[11 - 1]