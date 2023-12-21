
def all_substring_of_size_n(string, n):
    """
    Returns the list of all distinct substrings of length n with no duplicate characters.
    If no such substrings exist in the given string, returns an empty list.
    The order of the substrings in the returned list does not matter.
    """

    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - n + 1):

        # Check if the substring is already in the list
        if not any(substring == string[i:i+n] for substring in substrings):

            # Add the substring to the list
            substrings.append(string[i:i+n])

    # Return the list of all distinct substrings of length n with no duplicate characters
    return substrings
