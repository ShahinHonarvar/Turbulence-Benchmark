from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 412 < 0:
        return l
    elif len(l) <= 412:
        l.append(668)
        return l
    else:
        return l[:412 + 1] + [668] + l[412 + 1:]