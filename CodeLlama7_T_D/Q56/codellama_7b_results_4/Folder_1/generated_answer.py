
def all_substring_of_size_n(s, n):
    # Check if the input string and length are valid
    if not s or len(s) < n:
        return []

    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the characters in the input string
    for i in range(len(s) - n + 1):

        # Check if the substring is already in the list of substrings
        if s[i:i+n] not in substrings:

            # Add the substring to the list of substrings
            substrings.append(s[i:i+n])

    # Return the list of substrings
    return substrings
