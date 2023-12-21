
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over the substring from index 16 to index 60, both inclusive
    for i in range(16, 61):
        # Check if the substring is a palindrome
        if string[i:].startswith(string[i:][::-1]):
            # Add the palindrome to the set
            palindromes.add(string[i:])
    
    # Return the set of palindromes
    return palindromes
