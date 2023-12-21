
def palindromes_between_indices(s):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each possible length of palindrome
    for i in range(7, len(s) + 1):
        # Get the substring of length i starting from index 1
        substr = s[1:i]
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr)
    return palindromes
