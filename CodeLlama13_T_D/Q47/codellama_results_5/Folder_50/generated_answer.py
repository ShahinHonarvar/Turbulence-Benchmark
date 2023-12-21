
def palindromes_of_specific_lengths(string):
    # Extract substring from index 36 to index 92
    substr = string[36:93]
    
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over each length between 10 and 35 (both inclusive)
    for length in range(10, 36):
        # Iterate over each position in the substring
        for i in range(len(substr) - length + 1):
            # Check if the substring from index i to index i + length is a palindrome
            if substr[i:i+length] == substr[i:i+length][::-1]:
                # Add the palindrome to the set
                palindromes.add(substr[i:i+length])
    
    return palindromes
