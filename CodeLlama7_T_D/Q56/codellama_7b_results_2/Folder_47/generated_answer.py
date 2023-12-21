
def all_substring_of_size_n(s, n):
    # Check if the input string and size are valid
    if len(s) < n or n < 1:
        return []

    # Create a list to store the substrings
    substrings = []

    # Iterate over the length of the input string minus the size of the substring we want
    for i in range(len(s) - n + 1):

        # Check if the current substring is already in the list
        if s[i:i+n] not in substrings:

            # Add the current substring to the list
            substrings.append(s[i:i+n])

    # Return the list of substrings
    return substrings
