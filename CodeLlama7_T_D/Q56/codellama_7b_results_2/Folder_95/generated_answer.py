
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 79):

        # Check if the substring is of length 89 and contains no duplicate characters
        substring = string[i:i+89]
        if len(substring) == 89 and len(set(substring)) == 89:
            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of substrings
    return substrings
