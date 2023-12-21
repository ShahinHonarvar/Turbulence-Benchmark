
def palindromes_between_indices(s):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible substring of length at least 6
    for i in range(2, len(s) - 7 + 1):
        # Check if the substring is a palindrome
        if s[i:i+6] == s[i:i+6][::-1]:
            # Add the palindrome to the set
            palindromes.add(s[i:i+6])
    # Return the set of palindromes
    return palindromes
