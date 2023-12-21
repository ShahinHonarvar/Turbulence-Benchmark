
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the characters in the string
    for i in range(len(string) - 60)):
        # Extract a substring of length 61 from the string
        substring = string[i:i + 61]

        # Check if the substring has no duplicate characters
        if len(substring) == len(set(substring)):
            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of substrings
    return substrings
