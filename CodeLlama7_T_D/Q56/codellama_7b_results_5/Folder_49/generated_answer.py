
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 63):
        # Extract a substring of length 73 from the current position
        substring = string[i:i+73]

        # Check if the substring is valid (no duplicate characters)
        if len(substring) == 73 and all(substring.count(c) == 1 for c in 'abcdefghijklmnopqrstuvwxyz'):
            # Add the valid substring to the list
            substrings.append(substring)

    # Return the list of all distinct substrings
    return substrings
