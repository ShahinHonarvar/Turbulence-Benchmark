
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 4):

        # Check if the substring of length 5 exists in the current position of the loop
        if string[i:i + 5] in string:

            # If it does, add it to the list of substrings
            substrings.append(string[i:i + 5])

    # Return the list of substrings
    return substrings
