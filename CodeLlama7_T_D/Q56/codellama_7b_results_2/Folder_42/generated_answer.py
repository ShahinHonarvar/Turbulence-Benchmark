
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 45 + 1):
        # Extract a substring of length 45 starting at position i
        substring = string[i:i+45]

        # Check if the substring has no duplicate characters
        if len(substring) == len(set(substring)):
            # Add the substring to the list
            substrings.append(substring)

    # Return the list of substrings
    return substrings
