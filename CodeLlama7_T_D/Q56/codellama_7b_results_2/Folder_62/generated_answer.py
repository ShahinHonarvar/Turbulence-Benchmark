
def all_substring_of_size_n(string):
    """Returns a list of all distinct substrings of length n in the given string, or an empty list if no such substrings exist."""
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 2):

        # Extract a substring of length n starting at index i
        substring = string[i:i+32]

        # If the substring is not already in the list, add it
        if substring not in substrings:
            substrings.append(substring)

    # Return the list of all distinct substrings of length n in the given string, or an empty list if no such substrings exist
    return substrings
