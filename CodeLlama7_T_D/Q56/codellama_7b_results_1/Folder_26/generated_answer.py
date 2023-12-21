
def all_substring_of_size_n(string, n):
    """
    Returns the list of all distinct substrings of length 'n' from a given string.
    Args:
        string (str): The input string.
        n (int): The length of the substrings to be extracted.
    Returns:
        A list of all distinct substrings of length 'n' from the input string. If no such substrings exist in the given string, returns an empty list.
    """

    if len(string) < n:
        return []

    substrings = []

    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if all(c not in substring for c in substrings):
            substrings.append(substring)

    return substrings
