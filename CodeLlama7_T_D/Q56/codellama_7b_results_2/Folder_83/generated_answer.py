
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 47):

        # Check if the substring is of length 48 and contains no duplicate characters
        substring = string[i:i+48]
        if len(substring) == 48 and len(set(substring)) == 48:

            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 48 with no duplicate characters, or an empty list if none exist in the given string
    return substrings
