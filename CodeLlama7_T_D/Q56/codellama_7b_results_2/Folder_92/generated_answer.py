
def all_substring_of_size_n(s, n):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the characters in the input string
    for i in range(len(s) - n + 1):
        # Extract the current substring and add it to the list
        substrings.append(s[i:i+n])

    # Return the list of all distinct substrings
    return list(set(substrings)))
