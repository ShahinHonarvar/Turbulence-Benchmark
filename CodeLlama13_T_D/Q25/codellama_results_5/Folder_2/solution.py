from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 427 < 0 or len(l) <= 427:
        return l
    else:
        return l[:427] + [[312, 441]] + l[427:]