from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 323 < 0 or len(l) <= 323:
        return l
    else:
        return l[:323] + [[389, 303]] + l[323:]