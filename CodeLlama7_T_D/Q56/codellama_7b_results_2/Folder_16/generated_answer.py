
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate through each character in the string
    for i in range(len(string) - 123):

        # Check if the substring is already in the list
        if string[i:i+124] not in substrings:

            # Add the substring to the list
            substrings.append(string[i:i+124])

    # Return the list of all distinct substrings of length 124
    return substrings
