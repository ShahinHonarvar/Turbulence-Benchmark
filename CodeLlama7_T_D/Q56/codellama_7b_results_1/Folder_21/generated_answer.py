
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate through each character in the string
    for i in range(len(string) - 99):

        # Check if the substring of length 106 exists in the current position
        if string[i:i+106] == string[i:i+106]:

            # Add the substring to the list of substrings
            substrings.append(string[i:i+106])

    # Return the list of all distinct substrings
    return substrings
