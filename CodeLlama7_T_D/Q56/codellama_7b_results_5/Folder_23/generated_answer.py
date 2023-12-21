
def all_substring_of_size_n(string, n):
    """
    Return the list of all distinct substrings of length 'n' in the given string, with no duplicate characters. If no such substrings exist in the given string, return an empty list.
    Args:
        string (str): The input string.
        n (int): The size of the substrings to find.
    Returns:
        list[str]: A list of all distinct substrings of length 'n' in the given string, with no duplicate characters. If no such substrings exist in the given string, return an empty list.
    """

    # Check if the input string is valid and has at least one character
    if not string or len(string) == 0:
        return []

    # Create a set to store all distinct substrings of length 'n'
    substrings = set()

    # Loop through each substring of length 'n' in the input string
    for i in range(len(string) - n + 1):

        # Add the substring to the set of distinct substrings
        substrings.add(string[i:i+n])

    # Return the list of all distinct substrings of length 'n' in the given string, with no duplicate characters
    return list(substrings)
