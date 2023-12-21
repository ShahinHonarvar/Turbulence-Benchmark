
def all_substring_of_size_n(s):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate through each substring of length n in the given string
    for i in range(len(s) - 8):

        # Check if the current substring is a palindrome
        if s[i:i+9] == s[i:i+9][::-1]:

            # Add the palindromic substring to the list of substrings
            substrings.append(s[i:i+9])

    # Return the list of substrings
    return substrings
