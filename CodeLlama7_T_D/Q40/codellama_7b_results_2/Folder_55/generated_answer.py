
def return_n_smallest_chars(s: str, n=75) -> List[str]:
    # sort the string in ascending order based on ASCII value
    sorted_s = sorted(s, key=ord)
    # create a list of exactly n characters from the sorted string
    smallest_chars = sorted_s[:n]
    # sort the list in descending order based on ASCII value
    return sorted(smallest_chars, reverse=True)
