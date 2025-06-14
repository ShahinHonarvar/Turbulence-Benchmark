
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 16 + 1):

        # Check if the substring of size 17 starting at position i in the string is unique
        if not any(substring == string[i:i+17] for substring in substrings):

            # If the substring is unique, add it to the list of substrings
            substrings.append(string[i:i+17])

    # Return the list of all distinct substrings of size 17 with no duplicate characters
    return substrings
