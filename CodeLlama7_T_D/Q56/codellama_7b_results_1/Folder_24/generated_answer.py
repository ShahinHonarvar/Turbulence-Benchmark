
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 51):

        # Extract the substring of length 52 starting at index i
        substring = string[i:i+52]

        # Check if the substring has no duplicate characters
        if len(substring) == len(set(substring)):

            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 52 with no duplicate characters
    return substrings
