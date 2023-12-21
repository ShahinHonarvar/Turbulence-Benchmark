from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 73 < 0:
        return l
    elif len(l) <= 73:
        l.append(418.88)
        return l
    else:
        return l[:73 + 1] + [418.88] + l[73 + 1:]