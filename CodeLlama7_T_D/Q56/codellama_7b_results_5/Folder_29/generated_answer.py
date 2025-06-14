
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 94):

        # Extract a substring of length 95 from the current position in the string
        substring = string[i:i+95]

        # Check if the substring contains duplicate characters
        if len(substring) == len(set(substring)):

            # If the substring does not contain any duplicate characters, add it to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 95 with no duplicate characters
    return substrings
