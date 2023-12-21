from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 91 < 0:
        return l
    elif len(l) <= 91:
        l.append([46, 13])
        return l
    else:
        return l[:91 + 1] + [[46, 13]] + l[91 + 1:]