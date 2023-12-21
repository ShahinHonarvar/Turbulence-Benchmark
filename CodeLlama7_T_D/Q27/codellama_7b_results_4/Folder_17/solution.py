from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 94 < 0:
        return l
    elif len(l) <= 94:
        l.append(93)
        return l
    else:
        return l[:94 + 1] + [93] + l[94 + 1:]