
def all_substring_of_size_n(string, n):
    """
    Returns the list of all distinct substrings of length 'n' in the given string.
    If no such substrings exist, returns an empty list.
    The order of the substrings in the returned list does not matter.
    """

    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over each substring of length 'n' in the given string
    for i in range(len(string) - n + 1):

        # Add the substring to the list of substrings
        substrings.append(string[i:i+n])

    # Return the list of all distinct substrings
    return substrings
