
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 2):

        # Check if the substring of length 3 exists in the string
        if string[i:i + 3] in string:

            # Add the substring to the list if it does not already exist
            if string[i:i + 3] not in substrings:
                substrings.append(string[i:i + 3])

    # Return the list of distinct substrings
    return substrings
