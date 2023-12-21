
def palindrome_of_length_at_least_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each substring of length 45 or more in the string
    for i in range(len(string) - 44):
        substr = string[i:i+45]
        
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr)
    
    return palindromes
