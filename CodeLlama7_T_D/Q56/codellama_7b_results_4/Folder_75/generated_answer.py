
def all_substring_of_size_n(string, n):
    """
    Returns the list of all distinct substrings of the length equal to n with no duplicate characters.
    If no such substrings exist in the given string, the function should return an empty list.
    The order of the substrings in the returned list does not matter.
    """

    if len(string) < n:
        return []

    substrings = []

    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if all([c not in substrings for c in substring]) and not any([substring.count(c) > 1 for c in set(substring)])):
            substrings.append(substring)

    return substrings
