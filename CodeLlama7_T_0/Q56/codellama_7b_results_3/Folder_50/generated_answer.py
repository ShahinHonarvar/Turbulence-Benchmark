
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 10 + 1):

        # Check if the substring is of length 11 and has no duplicate characters
        substring = string[i:i+11]
        if len(substring) == 11 and len(set(substring)) == 11:

            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of substrings
    return substrings
