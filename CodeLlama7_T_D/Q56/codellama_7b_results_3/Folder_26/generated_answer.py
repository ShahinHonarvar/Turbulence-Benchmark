
def all_substring_of_size_n(s, n):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each substring of length n in the input string
    for i in range(len(s) - n + 1):
        # Add the current substring to the list of substrings
        substrings.append(s[i:i+n])

    # Return the list of all distinct substrings of length n
    return list(set(substrings)))```
