
def all_substring_of_size_n(s, n):
    # Check if the input string and substring size are valid
    if len(s) < n or n < 1:
        return []

    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate through each possible starting index of a substring
    for i in range(len(s) - n + 1):

        # Check if the substring at index i has length n
        if len(s[i:i+n]) == n:

            # Add the substring to the list of substrings
            substrings.append(s[i:i+n])

    # Return the list of substrings
    return substrings
