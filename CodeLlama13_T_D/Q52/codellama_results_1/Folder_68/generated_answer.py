
def palindrome_of_length_n(string):
    # Initialize a set to store the palindromes
    palindromes = set()
    
    # Loop through each substring of length 76
    for i in range(len(string) - 75):
        substr = string[i:i+76]
        
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr)
    
    # Return the set of palindromes
    return palindromes
