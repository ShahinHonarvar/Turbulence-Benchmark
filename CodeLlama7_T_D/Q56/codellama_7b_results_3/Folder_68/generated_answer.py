
def all_substring_of_size_n(string, n):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - n + 1):

        # Check if the substring is already in the list
        if string[i:i+n] not in substrings:

            # If it's not, add it to the list
            substrings.append(string[i:i+n])

    # Return the list of substrings
    return substrings
