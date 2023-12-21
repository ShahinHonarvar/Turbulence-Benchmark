
def all_substring_of_size_n(string, n):
    """Returns a list of all distinct substrings of length n with no duplicate characters in the given string. If no such substrings exist in the given string, the function should return an empty list. The order of the substrings in the returned list does not matter."""
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the characters in the string
    for i in range(len(string) - n + 1):
        # Extract the substring of length n starting at position i
        substring = string[i:i+n]
        # Check if the substring has no duplicate characters
        if len(substring) == len(set(substring)):
            # If the substring is distinct, add it to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length n with no duplicate characters in the given string
    return substrings
