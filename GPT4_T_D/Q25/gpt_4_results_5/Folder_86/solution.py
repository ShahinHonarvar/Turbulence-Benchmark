from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 990 < 0 or len(l) <= 990:
        return l
    else:
        return l[:990] + [[905, 742]] + l[990:]