
def all_substring_of_size_n(string):
    """
    Return the list of all distinct substrings of length n in the given string, or an empty list if no such substrings exist.
    Args:
        string (str): The input string.
    Returns:
        list[str]: The list of all distinct substrings of length n in the given string.
    """

    n = 17

    # Initialize an empty list to store the substrings

    substrings = []

    # Iterate through the characters in the input string

    for i in range(len(string) - n + 1):

        # Extract the substring of length n starting at index i

        substring = string[i:i+n]

        # Check if the substring is already in the list of substrings

        if substring not in substrings:

            # If it's not, add it to the list of substrings

            substrings.append(substring)

    return substrings
