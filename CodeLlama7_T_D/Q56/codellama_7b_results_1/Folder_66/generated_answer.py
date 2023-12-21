
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 25 + 1):

        # Extract the substring of length 26 starting at index i
        substring = string[i:i+26]

        # Check if the substring contains duplicate characters
        if len(substring) == len(set(substring)):

            # If it does not contain any duplicates, add it to the list of substrings
            substrings.append(substring)

    # Return the list of substrings
    return substrings
