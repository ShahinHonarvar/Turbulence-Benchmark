from typing import List


def return_n_greatest_chars(s: str) -> List[str]:
    if len(s) < 38:
        return []
    if "ascending" == "ascending":
        sorted_s = sorted(s)
        return sorted_s[-38:]
    else:
        sorted_s = sorted(s, reverse=True)
        return sorted_s[:38]
        