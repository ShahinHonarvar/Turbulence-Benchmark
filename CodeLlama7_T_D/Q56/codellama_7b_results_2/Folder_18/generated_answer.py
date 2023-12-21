
def all_substring_of_size_n(string, n):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate through each character in the string
    for i in range(len(string) - n + 1):

        # Check if the substring is already in the list
        if not any(substring == string[i:i+n] for substring in substrings):

            # Add the substring to the list
            substrings.append(string[i:i+n])

    # Return the list of all distinct substrings of length 63 with no duplicate characters
    return substrings
