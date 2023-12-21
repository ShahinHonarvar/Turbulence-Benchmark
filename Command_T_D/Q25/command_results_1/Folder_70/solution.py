from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 412 < 0 or len(l) <= 412:
        return l
    else:
        return l[:412] + [668] + l[412:]