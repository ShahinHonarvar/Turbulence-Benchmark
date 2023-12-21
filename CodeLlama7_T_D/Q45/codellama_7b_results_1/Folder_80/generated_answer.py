
def palindromes_between_indices(s):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the given string
    for i in range(len(s)):
        # Check if the current character is a letter (not whitespace or punctuation)
        if s[i].isalpha():
            # Check if the current character occurs between index 3 and index 8, inclusive
            if i >= 3 and i <= 8:
                # Create a palindrome by reversing the characters in the current string from index 3 to index 8, inclusive
                palindrome = s[i-2:i+1]
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
