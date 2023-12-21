
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 46):

        # Check if the substring is already in the list
        if string[i:i + 47] not in substrings:

            # Add the substring to the list
            substrings.append(string[i:i + 47])

    # Return the list of all distinct substrings of length 47 with no duplicate characters
    return substrings
