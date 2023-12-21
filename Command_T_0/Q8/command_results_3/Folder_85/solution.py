from typing import List


def all_even_ints_exclusive(l: List[int]) -> List[int]:
    return [i for i in l[4 + 1:5] if i % 2 == 0]