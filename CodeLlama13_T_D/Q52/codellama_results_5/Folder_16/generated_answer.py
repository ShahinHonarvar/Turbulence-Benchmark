
def palindrome_of_length_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate through each substring of length n in the string
    for i in range(len(string) - n + 1):
        substr = string[i:i+n]
        
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr)
            
    return palindromes
