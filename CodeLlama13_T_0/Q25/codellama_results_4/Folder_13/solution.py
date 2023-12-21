from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 693 < 0 or len(l) <= 693:
        return l
    else:
        return l[:693] + [[606, 873]] + l[693:]