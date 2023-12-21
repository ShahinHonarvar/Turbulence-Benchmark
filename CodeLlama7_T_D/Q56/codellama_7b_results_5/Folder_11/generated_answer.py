
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 78 + 1):
        # Extract the substring of length 78 starting at index i
        substring = string[i:i+78]

        # Check if the substring contains duplicate characters
        if len(substring) == len(set(substring)):
            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 78
    return substrings
