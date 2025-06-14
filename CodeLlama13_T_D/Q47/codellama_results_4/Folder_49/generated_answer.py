
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each substring of length 10 to 50 (both inclusive) in the string
    for i in range(10, 51):
        # Get the substring from index 10 to index 100 (both inclusive)
        substr = string[10:100]
        
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(substr)
    
    # Return the set of palindromes
    return palindromes
