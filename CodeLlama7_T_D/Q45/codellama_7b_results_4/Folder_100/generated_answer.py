
def palindromes_between_indices(s):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(s)):
        # Get the substring starting from index i and ending at index 5 (inclusive)
        substr = s[i:i+6]
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # Add the palindrome to the set of palindromes
            palindromes.add(substr)
    return palindromes
