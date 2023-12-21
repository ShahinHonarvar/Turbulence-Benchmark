
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 39):

        # Extract a substring of length 40 starting from the current character
        substring = string[i:i+40]

        # If the substring is not already in the list, add it
        if substring not in substrings:
            substrings.append(substring)

    # Return the list of all distinct substrings of length 40
    return substrings
