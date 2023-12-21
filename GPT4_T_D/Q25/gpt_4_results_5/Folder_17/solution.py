from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 94 < 0 or len(l) <= 94:
        return l
    else:
        return l[:94] + [93] + l[94:]