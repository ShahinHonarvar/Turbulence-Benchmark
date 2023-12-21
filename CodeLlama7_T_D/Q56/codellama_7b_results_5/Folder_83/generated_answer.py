
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 47):

        # Check if the substring is already in the list
        if string[i:i+48] not in substrings:

            # If it's not, add it to the list
            substrings.append(string[i:i+48])

    # Return the list of all distinct substrings of length 48
    return substrings
