
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the characters in the string
    for i in range(len(string) - 63)):
        # Extract a substring of length 64 from the current position
        substring = string[i:i+64]

        # Check if the substring has no duplicate characters
        if len(substring) == len(set(substring)):
            # Add the substring to the list
            substrings.append(substring)

    # Return the list of substrings
    return substrings
