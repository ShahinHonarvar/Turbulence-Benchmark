from typing import List


def all_even_ints_exclusive(l: List[int]) -> List[int]:
    return [i for i in l[78 + 1:93] if i % 2 == 0]