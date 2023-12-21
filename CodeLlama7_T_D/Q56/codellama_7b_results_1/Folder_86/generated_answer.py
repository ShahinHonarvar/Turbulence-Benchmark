
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 142):

        # Extract a substring of length 143 starting at index i
        substring = string[i:i+143]

        # Check if the substring has no duplicate characters
        if len(set(substring)) == 143:

            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of substrings
    return substrings
