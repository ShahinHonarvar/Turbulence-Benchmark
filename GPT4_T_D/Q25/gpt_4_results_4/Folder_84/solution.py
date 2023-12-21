from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 183 < 0 or len(l) <= 183:
        return l
    else:
        return l[:183] + [[148, 145]] + l[183:]