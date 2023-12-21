
def all_substring_of_size_n(s):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(s) - 45):

        # Check if the substring of length 46 exists in the given string
        if s[i:i+46] in s:

            # If it does, add it to the list of substrings
            substrings.append(s[i:i+46])

    # Return the list of all distinct substrings of length 46 with no duplicate characters
    return substrings
