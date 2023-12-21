from typing import List


def all_even_ints_exclusive(l: List[int]) -> List[int]:
    return [i for i in l[20 + 1:200] if i % 2 == 0]