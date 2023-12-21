
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 86):
        # Extract a substring of length 87 starting from the current index
        substring = string[i:i+87]

        # Check if the substring contains no duplicate characters
        if len(substring) == len(set(substring)):
            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of substrings
    return substrings
