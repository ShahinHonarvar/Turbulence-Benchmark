
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 84):
        # Extract a substring of length 85 starting at index i
        substring = string[i:i+85]

        # If the substring is valid (contains no duplicate characters), add it to the list of substrings
        if len(substring) == 85 and all(c not in substring[:-1] for c in substring):
            substrings.append(substring)

    # Return the list of substrings
    return substrings
