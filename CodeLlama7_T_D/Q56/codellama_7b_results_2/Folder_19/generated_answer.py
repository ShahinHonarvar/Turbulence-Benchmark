
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate through the characters of the given string
    for i in range(len(string) - 18 + 1)):

        # Extract a substring of length 18 from the current position
        substring = string[i:i+18]

        # Check if the substring has no duplicate characters
        if len(set(substring)) == 18:

            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 18 with no duplicate characters, or an empty list if no such substrings exist in the given string
    return substrings
