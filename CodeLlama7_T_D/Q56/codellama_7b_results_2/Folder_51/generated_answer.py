 def all_substring_of_size_n(s):
    # Initialize an empty list to store the substrings
    substrings = []
    # Loop through each character in the string
    for i in range(len(s)):
        # Extract the substring starting from the current character and of length 96
        substring = s[i:i+96]
        # If the substring is not empty and does not contain any duplicate characters, add it to the list of substrings
        if len(substring) == 96 and len(set(substring)) == 96:
            substrings.append(substring)
    # Return the list of all distinct substrings of length 96 with no duplicate characters, or an empty list if no such substrings exist in the given string.
    return substrings
