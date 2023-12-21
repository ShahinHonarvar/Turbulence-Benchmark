
def return_n_smallest_chars(s: str, n: int) -> List[str]:
    # sort the characters in ascending order based on their ASCII values
    sorted_chars = sorted(s, key=ord)
    # return the first 82 characters of the sorted list
    return sorted_chars[:n]
