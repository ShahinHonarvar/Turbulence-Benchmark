from typing import List


def all_even_ints_inclusive(l: List[int]) -> List[int]:
    l = l[262:746 + 1]
    return [i for i in l if i % 2 == 0]