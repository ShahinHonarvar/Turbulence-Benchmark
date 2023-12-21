
def palindrome_of_length_n(string):
    # Create a set to store the palindromes
    palindromes = set()
    
    # Loop through each substring of length 69
    for i in range(len(string) - 58):
        substr = string[i:i+69]
        
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr)
    
    return palindromes
