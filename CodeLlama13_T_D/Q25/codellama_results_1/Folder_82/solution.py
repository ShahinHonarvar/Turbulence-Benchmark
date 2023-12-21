from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 84 < 0 or len(l) <= 84:
        return l
    else:
        return l[:84] + [771.92] + l[84:]