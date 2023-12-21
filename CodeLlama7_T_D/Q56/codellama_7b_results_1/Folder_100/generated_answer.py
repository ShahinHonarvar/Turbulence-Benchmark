
def all_substring_of_size_n(string, n):
    # Check if the string has at least n characters
    if len(string) < n:
        return []

    # Create a list to store the substrings
    substrings = []

    # Iterate over all possible starting positions of a substring of length n
    for i in range(len(string) - n + 1):

        # Check if the current substring is already in the list
        if string[i:i+n] not in substrings:
            # Add the current substring to the list
            substrings.append(string[i:i+n])

    # Return the list of all distinct substrings of length n
    return substrings
