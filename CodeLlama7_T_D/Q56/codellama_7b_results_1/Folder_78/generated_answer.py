
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 48):

        # Extract a substring of length 49 starting at index i
        substring = string[i:i+49]

        # Check if the substring has no duplicate characters
        if len(substring) == len(set(substring)):

            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 49 with no duplicate characters, or an empty list if no such substrings exist in the given string
    return substrings
