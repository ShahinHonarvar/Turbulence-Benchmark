
def all_substring_of_size_n(s, n):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over each substring of length n in the input string s
    for i in range(len(s) - n + 1):
        # Add the substring to the list of substrings
        substrings.append(s[i:i+n])

    # Return the list of substrings
    return substrings
