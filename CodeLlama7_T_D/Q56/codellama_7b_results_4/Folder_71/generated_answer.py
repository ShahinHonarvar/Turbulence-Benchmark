
def all_substring_of_size_n(s, n):
    # Check if the input string and size are valid
    if len(s) < n or n <= 0:
        return []

    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the length of the input string
    for i in range(len(s) - n + 1):

        # Check if the current substring is already in the list
        if s[i:i+n] not in substrings:
            substrings.append(s[i:i+n])

    # Return the list of all distinct substrings
    return substrings
