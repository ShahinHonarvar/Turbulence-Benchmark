
def all_substring_of_size_n(s):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the characters in the string
    for i in range(len(s) - 5 + 1)):

        # Check if the substring is of length 6 and contains no duplicate characters
        if len(set(s[i:i+6])) == 6:

            # Add the substring to the list of substrings
            substrings.append(s[i:i+6])

    # Return the list of substrings
    return substrings
