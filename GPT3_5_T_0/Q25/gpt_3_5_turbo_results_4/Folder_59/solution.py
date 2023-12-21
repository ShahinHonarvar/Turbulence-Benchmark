from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 9 < 0 or len(l) <= 9:
        return l
    else:
        return l[:9] + [426.08] + l[9:]