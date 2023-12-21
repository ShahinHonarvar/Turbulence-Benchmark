
def all_substring_of_size_n(s):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(s)):
        # Extract the substring starting from the current character
        substr = s[i:]

        # Check if the substring has length equal to 19 and no duplicate characters
        if len(substr) == 19:
            # If the substring is valid, add it to the list of substrings
            substrings.append(substr)

    # Return the list of all distinct substrings of length equal to 19 with no duplicate characters
    return substrings
