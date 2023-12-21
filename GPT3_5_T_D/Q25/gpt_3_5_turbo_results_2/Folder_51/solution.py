from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 19 < 0 or len(l) <= 19:
        return l
    else:
        return l[:19] + [249.61] + l[19:]