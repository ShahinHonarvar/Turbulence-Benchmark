
def all_substring_of_size_n(string, n):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - n + 1):

        # Extract the substring of length n starting at index i
        substring = string[i:i+n]

        # Check if the substring has duplicate characters
        if len(substring) == len(set(substring)):

            # If the substring is unique, add it to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length n with no duplicate characters
    return substrings
