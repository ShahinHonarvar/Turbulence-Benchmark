from typing import List


def all_even_ints_exclusive(l: List[int]) -> List[int]:
    return [i for i in l[27 + 1:34] if i % 2 == 0]