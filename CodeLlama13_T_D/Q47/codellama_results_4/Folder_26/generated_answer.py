
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each substring of length 21-31 in the given string
    for i in range(21, 32):
        # Get the substring of length i from index 24 to index 84 (both inclusive)
        substr = string[24:85]
        
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr)
    
    # Return the set of palindromes
    return palindromes
