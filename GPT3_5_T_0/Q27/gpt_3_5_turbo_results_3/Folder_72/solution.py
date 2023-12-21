from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 24 < 0:
        return l
    elif len(l) <= 24:
        l.append([98, 22])
        return l
    else:
        return l[:24 + 1] + [[98, 22]] + l[24 + 1:]