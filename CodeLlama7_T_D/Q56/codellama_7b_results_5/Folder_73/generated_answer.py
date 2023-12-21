
def all_substring_of_size_n(s, n):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the length of the string
    for i in range(len(s) - n + 1):

        # Extract the substring of size n from the current position in the string
        substr = s[i:i+n]

        # Check if the substring is already in the list
        if substr not in substrings:

            # Add the substring to the list
            substrings.append(substr)

    # Return the list of all distinct substrings of size n
    return substrings
