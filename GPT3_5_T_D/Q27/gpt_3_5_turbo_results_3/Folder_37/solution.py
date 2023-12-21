from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 35 < 0:
        return l
    elif len(l) <= 35:
        l.append(88)
        return l
    else:
        return l[:35 + 1] + [88] + l[35 + 1:]