
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 58 + 1):

        # Extract a substring of length 68 from the current position
        substring = string[i:i+68]

        # If the substring is not already in the list, add it
        if substring not in substrings:
            substrings.append(substring)

    # Return the list of all distinct substrings of length 68
    return substrings
