
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 72):

        # Extract a substring of length 73 starting from index i
        substring = string[i:i+73]

        # Check if the substring contains duplicate characters
        if len(substring) == len(set(substring)):

            # Add the substring to the list if it does not contain any duplicate characters
            substrings.append(substring)

    # Return the list of all distinct substrings of length 73 with no duplicate characters
    return substrings
