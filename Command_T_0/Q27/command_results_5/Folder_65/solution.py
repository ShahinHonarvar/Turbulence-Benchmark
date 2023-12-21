from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 70 < 0:
        return l
    elif len(l) <= 70:
        l.append(185.43)
        return l
    else:
        return l[:70 + 1] + [185.43] + l[70 + 1:]