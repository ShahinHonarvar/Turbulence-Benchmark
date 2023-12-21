
def all_substring_of_size_n(s):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(s)):

        # Get the substring starting at index i and with length 100
        substr = s[i:i+100]

        # Check if the substring has no duplicate characters
        if len(set(substr)) == len(substr):

            # Add the substring to the list of substrings
            substrings.append(substr)

    # Return the list of all distinct substrings of length 100 with no duplicate characters, or an empty list if none exist
    return substrings
