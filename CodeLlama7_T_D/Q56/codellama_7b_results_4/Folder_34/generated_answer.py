
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 83):

        # Check if the substring of length 84 exists in the remaining part of the string
        if string[i:i + 84] in string[i + 1:]:

            # If it does, add it to the list of substrings
            substrings.append(string[i:i + 84])

    # Return the list of substrings
    return substrings
