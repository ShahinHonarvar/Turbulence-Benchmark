from typing import List


def return_n_greatest_chars(s: str) -> List[str]:
    if len(s) < 9:
        return []
    if "descending" == "ascending":
        sorted_s = sorted(s)
        return sorted_s[-9:]
    else:
        sorted_s = sorted(s, reverse=True)
        return sorted_s[:9]
        