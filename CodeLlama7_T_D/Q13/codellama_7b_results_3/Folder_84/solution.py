from typing import List


def find_second_largest_num(l: List[int]) -> int | None:
    l = l[43:86 + 1]
    if len(l) < 2:
        return None
    l.sort()
    return l[-2]