
def palindrome_of_length_n(string, n):
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over each substring of length n in the string
    for i in range(len(string) - n + 1):
        substr = string[i:i+n]
        
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr)
    
    # Return the set of palindromes
    return palindromes
