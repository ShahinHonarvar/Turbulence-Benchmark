from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 183 < 0:
        return l
    elif len(l) <= 183:
        l.append([148, 145])
        return l
    else:
        return l[:183 + 1] + [[148, 145]] + l[183 + 1:]