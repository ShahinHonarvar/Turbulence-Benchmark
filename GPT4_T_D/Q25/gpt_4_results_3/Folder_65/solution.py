from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 70 < 0 or len(l) <= 70:
        return l
    else:
        return l[:70] + [185.43] + l[70:]