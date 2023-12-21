from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 95 < 0:
        return l
    elif len(l) <= 95:
        l.append(43)
        return l
    else:
        return l[:95 + 1] + [43] + l[95 + 1:]