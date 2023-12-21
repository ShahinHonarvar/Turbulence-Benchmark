from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 983 < 0:
        return l
    elif len(l) <= 983:
        l.append(369)
        return l
    else:
        return l[:983 + 1] + [369] + l[983 + 1:]