from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 95 < 0 or len(l) <= 95:
        return l
    else:
        return l[:95] + [43] + l[95:]