from typing import List


def return_n_smallest_chars(s: str) -> List[str]:
    if len(s) < 69:
        return []
    if "ascending" == "ascending":
        sorted_s = sorted(s)
        return sorted_s[:69]
    else:
        sorted_s = sorted(s, reverse=True)
        return sorted_s[-69:]