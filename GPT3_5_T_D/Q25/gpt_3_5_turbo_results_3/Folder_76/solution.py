from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 166 < 0 or len(l) <= 166:
        return l
    else:
        return l[:166] + [232] + l[166:]