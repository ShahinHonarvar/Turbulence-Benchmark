from typing import List


def all_even_ints_exclusive(l: List[int]) -> List[int]:
    return [i for i in l[100 + 1:101] if i % 2 == 0]