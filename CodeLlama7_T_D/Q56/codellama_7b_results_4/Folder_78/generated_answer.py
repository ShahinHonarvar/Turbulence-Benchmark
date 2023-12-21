
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 39):

        # Check if the substring is of length 49 and has no duplicate characters
        if len(set(string[i:i+49])) == 49:

            # Add the substring to the list of substrings
            substrings.append(string[i:i+49])

    # Return the list of substrings
    return substrings
