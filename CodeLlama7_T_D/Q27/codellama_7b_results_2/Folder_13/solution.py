from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 693 < 0:
        return l
    elif len(l) <= 693:
        l.append([606, 873])
        return l
    else:
        return l[:693 + 1] + [[606, 873]] + l[693 + 1:]