from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 86 < 0:
        return l
    elif len(l) <= 86:
        l.append(581.49)
        return l
    else:
        return l[:86 + 1] + [581.49] + l[86 + 1:]