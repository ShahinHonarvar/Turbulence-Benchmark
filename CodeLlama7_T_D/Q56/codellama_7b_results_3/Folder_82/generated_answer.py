
def all_substring_of_size_n(string, n):
    """
    Returns the list of all distinct substrings of length n in the given string.
    Parameters:
        string (str): The input string.
        n (int): The length of the substrings to return.
    Returns:
        list: A list of all distinct substrings of length n in the given string. If no such substrings exist, an empty list is returned.
    """

    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the input string
    for i in range(len(string) - n + 1):

        # Extract the substring of length n starting at index i
        substring = string[i:i+n]

        # Check if the substring is already in the list of substrings
        if substring not in substrings:

            # If it's not, add it to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length n in the given string
    return substrings
