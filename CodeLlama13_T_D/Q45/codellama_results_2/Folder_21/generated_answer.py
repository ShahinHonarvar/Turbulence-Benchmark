
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each possible 7-letter substring of the string
    for i in range(1, len(string) - 6):
        substr = string[i:i+7]
        
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr)
    
    # Return the set of all palindromes found
    return palindromes
