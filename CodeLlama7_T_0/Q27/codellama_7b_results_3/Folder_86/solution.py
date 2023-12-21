from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 990 < 0:
        return l
    elif len(l) <= 990:
        l.append([905, 742])
        return l
    else:
        return l[:990 + 1] + [[905, 742]] + l[990 + 1:]