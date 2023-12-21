from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 18 < 0:
        return l
    elif len(l) <= 18:
        l.append(742.2)
        return l
    else:
        return l[:18 + 1] + [742.2] + l[18 + 1:]