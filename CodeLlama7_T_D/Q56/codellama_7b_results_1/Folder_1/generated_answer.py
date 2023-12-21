
def all_substring_of_size_n(string, n):
    # Check if the input string is valid
    if not isinstance(string, str) or len(string) == 0:
        return []

    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the characters in the input string
    for i in range(len(string) - n + 1):

        # Check if the substring is unique and does not contain any duplicates
        if all(c not in substrings for c in string[i:i+n])):
            substrings.append(string[i:i+n])

    return substrings
