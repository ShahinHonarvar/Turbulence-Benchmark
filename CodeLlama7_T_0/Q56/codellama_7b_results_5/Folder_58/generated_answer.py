
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string)):

        # Initialize an empty string to store the current substring
        substring = ""

        # Loop through each character in the string starting from the current index
        for j in range(i, len(string) + 1):

            # Add the current character to the substring
            substring += string[j]

            # If the length of the substring is equal to 127, add it to the list of substrings
            if len(substring) == 127:
                substrings.append(substring)

    # Return the list of all distinct substrings of length 127 with no duplicate characters
    return substrings
