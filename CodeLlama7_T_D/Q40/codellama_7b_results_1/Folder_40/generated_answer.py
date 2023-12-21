
def return_n_smallest_chars(s: str, n: int) -> list[str]:
    # Sort the characters in the string by their ASCII values
    sorted_chars = sorted(s, key=ord)
    # Return the first `n` characters of the sorted list
    return sorted_chars[:n]
