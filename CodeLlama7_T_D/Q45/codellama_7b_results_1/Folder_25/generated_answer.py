
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible sub-string of length at least 3 in the given string
    for i in range(1, len(string) - 2):
        # Check if the current sub-string is a palindrome
        if string[i] == string[i+1]:
            # Add the palindrome to the set
            palindromes.add(string[i:i+3])
    # Return the set of all palindromes of length at least 3 that can be created from the English letters of the given string in the specified range
    return palindromes
