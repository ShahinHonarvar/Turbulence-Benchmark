
def all_substring_of_size_n(s, n):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the length of the string
    for i in range(len(s) - n + 1):

        # Check if the substring is already in the list
        if s[i:i+n] not in substrings:

            # Add the substring to the list
            substrings.append(s[i:i+n])

    return substrings
