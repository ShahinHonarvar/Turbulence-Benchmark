
def all_substring_of_size_n(s):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(s)):

        # Extract the substring starting at index i and of length 26
        substring = s[i:i+26]

        # Check if the substring is valid (i.e., it contains no duplicate characters)
        if len(substring) == 26 and len(set(substring)) == 26:

            # If the substring is valid, add it to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 26 with no duplicate characters, or an empty list if no such substrings exist in the given string
    return substrings
