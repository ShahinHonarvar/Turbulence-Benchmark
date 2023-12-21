from typing import List


def all_even_ints_exclusive(l: List[int]) -> List[int]:
    return [i for i in l[15 + 1:40] if i % 2 == 0]