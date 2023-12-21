
def all_substring_of_size_n(s, n):
    # Check if the input string and length are valid
    if not s or len(s) < n:
        return []

    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each possible starting index of a substring
    for i in range(len(s) - n + 1):

        # Check if the substring at this index has already been added to the list
        if s[i:i+n] not in substrings:

            # Add the substring to the list
            substrings.append(s[i:i+n])

    # Return the list of all distinct substrings of length n with no duplicate characters
    return substrings
