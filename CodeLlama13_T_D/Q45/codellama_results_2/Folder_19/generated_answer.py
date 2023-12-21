
def palindromes_between_indices(string):
    # Initialize a set to store the palindromes
    palindromes = set()
    
    # Loop through each substring of length 7 in the given string
    for i in range(len(string) - 6):
        substr = string[i:i+7]
        
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            palindromes.add(substr)
    
    # Return the set of palindromes
    return palindromes
