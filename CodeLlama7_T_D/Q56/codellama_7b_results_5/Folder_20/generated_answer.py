
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 49):
        # Extract a substring of length 50 starting from the current character
        substring = string[i:i + 50]

        # Check if the substring has no duplicate characters
        if len(substring) == len(set(substring)):
            # If the substring is unique, add it to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 50 with no duplicate characters
    return substrings
