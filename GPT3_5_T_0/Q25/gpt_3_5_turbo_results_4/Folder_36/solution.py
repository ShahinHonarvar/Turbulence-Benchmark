from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 361 < 0 or len(l) <= 361:
        return l
    else:
        return l[:361] + [[699, 556]] + l[361:]