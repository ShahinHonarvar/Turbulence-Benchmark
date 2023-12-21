
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate through each character in the string
    for i in range(len(string) - 4):

        # Check if the substring of length 5 exists in the string
        if string[i:i+5] in string:

            # Add the substring to the list of substrings
            substrings.append(string[i:i+5])

    # Return the list of all distinct substrings of length 5
    return substrings
