
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 66):
        # Extract a substring of length 77 starting from the current index
        substring = string[i:i+77]

        # Check if the substring has no duplicate characters
        if len(substring) == len(set(substring)):
            # If the substring is unique, add it to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 77 with no duplicate characters
    return substrings
