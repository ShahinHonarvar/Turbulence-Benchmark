
def palindrome_of_length_n(s):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each substring of length 97 in s
    for i in range(len(s) - 96):
        substr = s[i:i+97]
        
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr)
    
    # Return the set of palindromes
    return palindromes
