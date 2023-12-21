from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 427 < 0:
        return l
    elif len(l) <= 427:
        l.append([312, 441])
        return l
    else:
        return l[:427 + 1] + [[312, 441]] + l[427 + 1:]