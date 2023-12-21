from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 361 < 0:
        return l
    elif len(l) <= 361:
        l.append([699, 556])
        return l
    else:
        return l[:361 + 1] + [[699, 556]] + l[361 + 1:]