
def all_substring_of_size_n(s):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each substring of length 100 in the input string s
    for i in range(len(s) - 99):
        # Extract the current substring from the input string
        curr_substring = s[i:i+100]

        # Check if the current substring has any duplicate characters
        if len(curr_substring) == len(set(curr_substring)):
            # If the current substring does not have any duplicate characters, add it to the list of substrings
            substrings.append(curr_substring)

    # Return the list of all distinct substrings of length 100 with no duplicate characters in the input string s
    return substrings
