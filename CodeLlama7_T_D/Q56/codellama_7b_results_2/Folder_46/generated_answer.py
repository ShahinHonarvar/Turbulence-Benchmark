 def all_substring_of_size_n(string):
    # Initialize an empty list to store substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 86):

        # Extract a substring of length 87 starting at position i
        substring = string[i:i+87]

        # Check if the substring contains duplicate characters
        if len(substring) == len(set(substring)):

            # If the substring is valid, add it to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 87
    return substrings
