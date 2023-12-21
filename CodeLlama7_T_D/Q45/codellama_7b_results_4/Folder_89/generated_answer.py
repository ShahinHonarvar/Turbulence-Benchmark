
def palindromes_between_indices(s):
    # Create a set to store the palindromes
    palindromes = set()
    # Iterate over all possible substrings of length 6 or more
    for i in range(len(s) - 5):
        # Get the substring starting at index i and ending at index i + 5
        substr = s[i:i + 6]
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr)
    return palindromes
