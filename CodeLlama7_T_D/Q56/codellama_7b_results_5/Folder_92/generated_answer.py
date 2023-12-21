
def all_substring_of_size_n(s):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(s)):

        # Initialize a variable to keep track of the current substring
        curr_substring = ""

        # Loop through each character in the string starting from the current index
        for j in range(i, len(s) + 1):

            # Add the current character to the current substring
            curr_substring += s[j - 1]

            # If the length of the current substring is equal to the desired size (9), add it to the list of substrings
            if len(curr_substring) == 9:
                substrings.append(curr_substring)

        # Remove duplicates from the list of substrings using the 'set' data structure
        substrings = list(set(substrings))

    # Return the list of substrings, or an empty list if no such substrings exist in the given string
    return substrings
