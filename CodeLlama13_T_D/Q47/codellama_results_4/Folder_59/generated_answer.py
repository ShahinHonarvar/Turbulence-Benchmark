
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each substring of length 3 to 15
    for i in range(3, 16):
        # Get the substring starting from index 0 and ending at index i
        substr = string[0:i]
        
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr)
    
    # Return the set of palindromes
    return palindromes
