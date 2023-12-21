
def palindromes_between_indices(s):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each substring in the given string
    for i in range(len(s) - 6 + 1):
        # Check if the substring is a palindrome
        if s[i:i+7] == s[i:i+7][::-1]:
            # Add the palindrome to the set
            palindromes.add(s[i:i+7])
    # Return the set of all palindromes
    return palindromes
