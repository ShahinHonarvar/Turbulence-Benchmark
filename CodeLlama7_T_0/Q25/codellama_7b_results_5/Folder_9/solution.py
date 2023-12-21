from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 66 < 0 or len(l) <= 66:
        return l
    else:
        return l[:66] + [45] + l[66:]