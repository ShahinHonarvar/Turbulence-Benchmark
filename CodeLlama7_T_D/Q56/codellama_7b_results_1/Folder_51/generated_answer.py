
def all_substring_of_size_n(s):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate through the characters of the string
    for i in range(len(s) - 95):

        # Extract a substring of length 96 from the string
        substring = s[i:i+96]

        # Check if the substring has no duplicate characters
        if len(substring) == len(set(substring)):

            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of substrings
    return substrings
