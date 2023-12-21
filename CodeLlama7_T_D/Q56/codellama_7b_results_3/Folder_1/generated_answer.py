
def all_substring_of_size_n(string, n):
    # Check if the input string and size are valid
    if len(string) < n or n < 1:
        return []

    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate through the characters of the input string
    for i in range(len(string) - n + 1):
        # Check if the current substring is a duplicate
        if not any(substring == substrings[j] for j in range(len(substrings))):
            # Add the current substring to the list of substrings
            substrings.append(string[i:i+n])

    # Return the list of all distinct substrings of length n
    return substrings
