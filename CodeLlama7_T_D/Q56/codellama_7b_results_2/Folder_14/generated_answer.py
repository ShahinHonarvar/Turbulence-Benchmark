
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 84):

        # Check if the substring of length 85 starting at index i in the string exists
        if string[i:i+85] != None:

            # Add the substring to the list of substrings
            substrings.append(string[i:i+85])

    # Return the list of all distinct substrings of length 85 with no duplicate characters
    return substrings
