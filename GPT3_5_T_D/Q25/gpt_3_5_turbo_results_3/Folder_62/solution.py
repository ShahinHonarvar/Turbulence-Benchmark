from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 35 < 0 or len(l) <= 35:
        return l
    else:
        return l[:35] + [[90, 76]] + l[35:]