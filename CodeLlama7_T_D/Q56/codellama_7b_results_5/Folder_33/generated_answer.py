
def all_substring_of_size_n(s):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(s)):
        # Get the substring starting from the current character
        substring = s[i:]

        # Check if the substring has length equal to 105
        if len(substring) == 105:
            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of substrings
    return substrings
