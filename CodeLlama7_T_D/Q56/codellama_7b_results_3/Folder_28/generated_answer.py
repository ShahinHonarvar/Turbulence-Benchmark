
def all_substring_of_size_n(string, n):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the characters in the string
    for i in range(len(string) - n + 1):

        # Check if the substring is unique and does not contain any duplicate characters
        if all(c not in substrings for c in string[i:i+n]):

            # Add the substring to the list of substrings
            substrings.append(string[i:i+n])

    # Return the list of substrings
    return substrings
