from typing import List


def all_even_ints_exclusive(l: List[int]) -> List[int]:
    return [i for i in l[86 + 1:89] if i % 2 == 0]