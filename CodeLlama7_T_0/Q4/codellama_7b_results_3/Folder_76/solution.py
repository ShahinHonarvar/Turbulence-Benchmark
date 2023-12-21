from typing import List


def all_pos_ints_exclusive(l: List[int]) -> List[int]:
    return [i for i in l[361 + 1:643] if i > 0]
