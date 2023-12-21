from typing import List


def return_n_smallest_chars(s: str) -> List[str]:
    if len(s) < 23:
        return []
    if "ascending" == "ascending":
        sorted_s = sorted(s)
        return sorted_s[:23]
    else:
        sorted_s = sorted(s, reverse=True)
        return sorted_s[-23:]