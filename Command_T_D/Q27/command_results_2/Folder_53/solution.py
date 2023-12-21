from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 92 < 0:
        return l
    elif len(l) <= 92:
        l.append(709.87)
        return l
    else:
        return l[:92 + 1] + [709.87] + l[92 + 1:]