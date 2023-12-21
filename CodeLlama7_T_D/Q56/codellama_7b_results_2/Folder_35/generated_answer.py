
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 27 + 1):

        # Extract a substring of length 27 from the current position
        substring = string[i:i+27]

        # Check if the substring has no duplicate characters
        if len(substring) == len(set(substring)):

            # Add the substring to the list if it is unique
            substrings.append(substring)

    # Return the list of all distinct substrings of length 27 with no duplicate characters
    return substrings
