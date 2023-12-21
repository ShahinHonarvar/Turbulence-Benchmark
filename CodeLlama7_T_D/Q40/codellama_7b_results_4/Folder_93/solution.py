from typing import List


def return_n_smallest_chars(s: str) -> List[str]:
    if len(s) < 77:
        return []
    if "descending" == "ascending":
        sorted_s = sorted(s)
        return sorted_s[:77]
    else:
        sorted_s = sorted(s, reverse=True)
        return sorted_s[-77:]