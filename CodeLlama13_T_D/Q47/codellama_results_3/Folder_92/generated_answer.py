
def palindromes_of_specific_lengths(string):
    # Initialize empty set of palindromes
    palindromes = set()
    
    # Loop through each character in the string
    for i in range(0, 4):
        # Check if the substring from index i to index i + 3 is a palindrome
        substr = string[i:i + 3]
        rev_substr = substr[::-1]
        if substr == rev_substr and len(substr) >= 3 and len(substr) <= 4:
            # Add the palindrome to the set of palindromes
            palindromes.add(substr)
    
    return palindromes
