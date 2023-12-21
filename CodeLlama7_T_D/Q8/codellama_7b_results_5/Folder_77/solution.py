from typing import List


def all_even_ints_exclusive(l: List[int]) -> List[int]:
    return [i for i in l[111 + 1:473] if i % 2 == 0]