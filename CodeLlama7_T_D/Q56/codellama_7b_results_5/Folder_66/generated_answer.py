
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 25 + 1):

        # Extract a substring of length 26 from the current position in the string
        substring = string[i:i+26]

        # Check if the substring has no duplicate characters
        if len(substring) == len(set(substring)):

            # Add the substring to the list of substrings if it is not already present
            if substring not in substrings:
                substrings.append(substring)

    # Return the list of all distinct substrings of length 26 with no duplicate characters, or an empty list if no such substrings exist in the given string
    return substrings
