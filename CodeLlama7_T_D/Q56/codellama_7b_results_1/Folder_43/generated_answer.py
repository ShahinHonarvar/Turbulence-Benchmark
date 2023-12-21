
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 85)):
        # Extract the substring of length 86 starting from the current character
        substring = string[i:i+86]

        # Check if the substring has no duplicate characters
        if len(set(substring)) == 86:
            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 86 with no duplicate characters, or an empty list if no such substrings exist in the given string
    return substrings
