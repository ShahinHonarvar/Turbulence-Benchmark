
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 96):

        # Check if the substring is already in the list
        if string[i:i+97] not in substrings:

            # If it's not, add it to the list
            substrings.append(string[i:i+97])

    # Return the list of substrings
    return substrings
