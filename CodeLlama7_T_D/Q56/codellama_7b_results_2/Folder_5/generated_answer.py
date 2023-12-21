
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 63)):
        # Extract a substring of length 64 starting at index i
        substring = string[i:i+64]

        # Check if the substring has no duplicate characters
        if len(set(substring)) == 64:
            # Add the substring to the list
            substrings.append(substring)

    # Return the list of all distinct substrings of length 64 with no duplicate characters, or an empty list if no such substrings exist in the given string
    return substrings
