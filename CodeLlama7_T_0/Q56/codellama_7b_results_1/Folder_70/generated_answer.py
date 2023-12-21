
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 12 + 1):

        # Check if the substring is of length 12 and has no duplicate characters
        substring = string[i:i+12]
        if len(substring) == 12 and len(set(substring)) == 12:

            # If the substring is valid, add it to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 12 with no duplicate characters
    return substrings
