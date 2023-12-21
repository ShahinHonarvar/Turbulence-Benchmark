
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 80):

        # Extract a substring of length 81 starting at position i
        substring = string[i:i+81]

        # Check if the substring contains duplicate characters
        if len(substring) == len(set(substring)):
            substrings.append(substring)

    # Return the list of all distinct substrings of length 81 with no duplicate characters, or an empty list if no such substrings exist in the given string
    return substrings
