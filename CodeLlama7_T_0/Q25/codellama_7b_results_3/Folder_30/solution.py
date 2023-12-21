from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 18 < 0 or len(l) <= 18:
        return l
    else:
        return l[:18] + [742.2] + l[18:]