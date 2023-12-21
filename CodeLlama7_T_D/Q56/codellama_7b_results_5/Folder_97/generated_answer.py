
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 142 + 1):

        # Extract the substring of length 142 starting at position i
        substring = string[i:i+142]

        # Check if the substring has no duplicate characters
        if len(set(substring)) == 142:

            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 142
    return substrings
