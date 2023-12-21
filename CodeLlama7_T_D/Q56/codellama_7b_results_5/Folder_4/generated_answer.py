
def all_substring_of_size_n(string):
    """Returns a list of all distinct substrings of length n in the given string, where n is equal to 41."""
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 39):

        # Extract a substring of length 41 starting at index i
        substring = string[i:i + 41]

        # If the substring is not already in the list of substrings, add it to the list
        if substring not in substrings:
            substrings.append(substring)

    # Return the list of all distinct substrings of length 41 in the given string, or an empty list if no such substrings exist
    return substrings
