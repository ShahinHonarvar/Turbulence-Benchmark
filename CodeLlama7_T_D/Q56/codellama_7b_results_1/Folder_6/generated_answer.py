
def all_substring_of_size_n(string, n):
    """
    Return the list of all distinct substrings of length 'n' in the given string 'string'.
    Args:
        string (str): The input string.
        n (int): The length of the substrings to be returned.
    Returns:
        A list of all distinct substrings of length 'n' in the given string 'string'.
        If no such substrings exist in the given string, an empty list is returned.
    """

    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the characters in the input string
    for i in range(len(string) - n + 1):

        # Extract the substring of length 'n' starting from index 'i'
        substring = string[i:i+n]

        # Check if the substring is already present in the list
        if substring not in substrings:

            # Add the substring to the list
            substrings.append(substring)

    return substrings
