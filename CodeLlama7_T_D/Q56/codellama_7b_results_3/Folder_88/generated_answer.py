
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 68 + 1):
        # Extract a substring of length 68 from the current position
        substring = string[i:i+68]

        # Check if the substring contains any duplicate characters
        if len(substring) == len(set(substring)):
            # If it does not contain any duplicates, add it to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 68 with no duplicate characters
    return substrings
