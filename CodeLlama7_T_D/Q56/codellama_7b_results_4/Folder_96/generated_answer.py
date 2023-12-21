
def all_substring_of_size_n(s, n):
    # Check if the input string is valid
    if not s or len(s) < n:
        return []

    # Initialize the list of substrings
    substrings = []

    # Iterate over the length of the input string
    for i in range(len(s) - n + 1):

        # Check if the current substring is distinct and has no duplicate characters
        if all(c not in substrings for c in s[i:i+n]):

            # Add the current substring to the list of substrings
            substrings.append(s[i:i+n])

    # Return the list of substrings
    return substrings
