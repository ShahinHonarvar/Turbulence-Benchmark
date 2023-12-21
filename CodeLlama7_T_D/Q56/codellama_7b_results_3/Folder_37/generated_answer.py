
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 5 + 1)):
        # Extract a substring of length 65 from the current position
        substring = string[i:i+65]

        # Check if the substring has no duplicate characters
        if len(substring) == len(set(substring)):
            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of substrings
    return substrings
