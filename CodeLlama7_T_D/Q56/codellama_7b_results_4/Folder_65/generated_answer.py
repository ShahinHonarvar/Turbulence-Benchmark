
def all_substring_of_size_n(string, n=81):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - n + 1):
        # Extract the substring of length n starting at index i
        substring = string[i:i+n]

        # If the substring has no duplicate characters, add it to the list of substrings
        if len(substring) == len(set(substring)):
            substrings.append(substring)

    # Return the list of all distinct substrings of length 81 with no duplicate characters
    return substrings
