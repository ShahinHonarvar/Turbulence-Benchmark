from typing import List


def return_n_smallest_chars(s: str) -> List[str]:
    if len(s) < 87:
        return []
    if "descending" == "ascending":
        sorted_s = sorted(s)
        return sorted_s[:87]
    else:
        sorted_s = sorted(s, reverse=True)
        return sorted_s[-87:]