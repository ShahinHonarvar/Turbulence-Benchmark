
def all_substring_of_size_n(string):
    """Returns a list of all distinct substrings of the length equal to 64 with no duplicate characters. If no such substrings exist in the given string, the function should return an empty list."""
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 63):

        # Extract a substring of length 64 from the current character in the string
        substring = string[i:i+64]

        # Check if the substring has no duplicate characters
        if len(substring) == len(set(substring)):

            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of substrings
    return substrings
