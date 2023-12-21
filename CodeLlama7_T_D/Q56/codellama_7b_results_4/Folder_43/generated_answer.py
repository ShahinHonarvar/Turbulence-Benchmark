
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 85)):

        # Extract a substring of length 86 from the current position
        substring = string[i:i+86]

        # Check if the substring contains duplicate characters
        if len(substring) == len(set(substring)):

            # Add the substring to the list if it does not already exist
            if substring not in substrings:
                substrings.append(substring)

    # Return the list of substrings
    return substrings
