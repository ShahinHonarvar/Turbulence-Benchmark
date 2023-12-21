
def all_substring_of_size_n(s):
    # Create an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(s)):

        # Start a new substring with the current character
        substring = s[i]

        # Add the current character to the substring
        substring += s[i + 1]

        # Add the substring to the list of substrings if it is of size n
        if len(substring) == 11:
            substrings.append(substring)

    # Return the list of substrings
    return substrings
