from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 73 < 0 or len(l) <= 73:
        return l
    else:
        return l[:73] + [418.88] + l[73:]