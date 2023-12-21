from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 89 < 0 or len(l) <= 89:
        return l
    else:
        return l[:89] + [86] + l[89:]