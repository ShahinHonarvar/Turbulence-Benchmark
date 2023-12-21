
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 99):

        # Extract a substring of length 105 starting at index i
        substring = string[i:i+105]

        # Check if the substring is already in the list of substrings
        if substring not in substrings:

            # If it's not, add it to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 105 with no duplicate characters
    return substrings
