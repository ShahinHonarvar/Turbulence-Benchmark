
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 54):

        # Extract a substring of length 55 starting from the current character
        substring = string[i:i+55]

        # Check if the substring has no duplicate characters
        if len(substring) == len(set(substring)):

            # Add the substring to the list if it is not already present
            if substring not in substrings:
                substrings.append(substring)

    # Return the list of all distinct substrings of length 55 with no duplicate characters
    return substrings
