
def return_nth_smallest_ascii(s: str) -> str:
    subset = s[18:46]
    sorted_subset = sorted(subset)
    return sorted_subset[6]
