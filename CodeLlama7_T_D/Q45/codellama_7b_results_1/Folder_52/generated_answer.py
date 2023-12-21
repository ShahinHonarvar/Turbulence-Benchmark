
def palindromes_between_indices(s):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring in the given string
    for i in range(len(s) - 6 + 1):
        # Check if the current substring is a palindrome
        if s[i:i+7] == s[i:i+7][::-1]:
            # Add the palindrome to the set
            palindromes.add(s[i:i+7])
    # Return the set of palindromes
    return palindromes
