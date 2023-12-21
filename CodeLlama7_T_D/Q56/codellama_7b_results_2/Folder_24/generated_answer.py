
def all_substring_of_size_n(string, n):
    """
    Return the list of all distinct substrings of length n in the given string.
    If no such substrings exist in the given string, return an empty list.
    The order of the substrings in the returned list does not matter.
    """

    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - n + 1):
        # Extract the substring of length n starting from the current character
        substring = string[i:i+n]

        # If the substring is not already in the list, add it
        if substring not in substrings:
            substrings.append(substring)

    # Return the list of all distinct substrings of length n in the given string
    return substrings
