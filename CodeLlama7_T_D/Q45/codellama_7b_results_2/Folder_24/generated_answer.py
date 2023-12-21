
def palindromes_between_indices(s):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring in the given string that is at least 4 characters long
    for i in range(2, len(s) - 1):
        # Check if the current substring is a palindrome
        if s[i] == s[i:].lower():
            # Add the palindrome to the set of palindromes
            palindromes.add(s[i])
    # Return the set of palindromes
    return palindromes
