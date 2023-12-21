from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 62 < 0 or len(l) <= 62:
        return l
    else:
        return l[:62] + [51] + l[62:]