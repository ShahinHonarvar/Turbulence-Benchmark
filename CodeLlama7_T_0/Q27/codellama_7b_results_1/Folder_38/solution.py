from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 89 < 0:
        return l
    elif len(l) <= 89:
        l.append(86)
        return l
    else:
        return l[:89 + 1] + [86] + l[89 + 1:]