
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 56 + 1):

        # Extract a substring of length 56 from the current position
        substring = string[i:i+56]

        # If the substring has no duplicate characters, add it to the list
        if len(substring) == 56 and len(set(substring)) == 56:
            substrings.append(substring)

    # Return the list of substrings
    return substrings
