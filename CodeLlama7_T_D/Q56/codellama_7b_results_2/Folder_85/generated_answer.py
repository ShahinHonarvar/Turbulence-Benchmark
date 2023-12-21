
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate through each character in the string
    for i in range(len(string) - 14 + 1):
        # Extract a substring of length 14 starting from index i
        substring = string[i:i+14]

        # Check if the substring is valid (i.e., it has no duplicate characters)
        if len(set(substring)) == 14:
            # Add the valid substring to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 14 with no duplicate characters
    return substrings
