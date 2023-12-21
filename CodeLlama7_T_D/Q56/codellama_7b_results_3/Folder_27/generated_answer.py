
def all_substring_of_size_n(string, n):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the characters in the string
    for i in range(len(string) - n + 1):

        # Check if the substring is already in the list
        if string[i:i+n] not in substrings:

            # Add the substring to the list
            substrings.append(string[i:i+n])

    # Return the list of all distinct substrings of length n
    return substrings
