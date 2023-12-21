from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 983 < 0 or len(l) <= 983:
        return l
    else:
        return l[:983] + [369] + l[983:]