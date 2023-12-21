
def palindromes_of_specific_lengths(string):
    # Get the substring from index 23 to index 82, both inclusive
    substr = string[23:83]
    
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over each length between 32 and 34 (both inclusive)
    for length in range(32, 35):
        # Iterate over each substring of the given length
        for i in range(len(substr)):
            # Check if the substring is a palindrome
            if substr[i:i+length] == substr[i:i+length][::-1]:
                # Add the palindrome to the set
                palindromes.add(substr[i:i+length])
    
    return palindromes
