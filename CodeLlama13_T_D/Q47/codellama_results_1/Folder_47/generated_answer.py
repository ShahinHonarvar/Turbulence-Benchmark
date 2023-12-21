
def palindromes_of_specific_lengths(string):
    # Extract the substring of interest
    substr = string[39:95]
    
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each length between 14 and 52 (both inclusive)
    for length in range(14, 53):
        # Iterate over each starting index in the substring
        for i in range(len(substr) - length + 1):
            # Check if the substring from index i to index i + length is a palindrome
            if substr[i:i+length] == substr[i:i+length][::-1]:
                # If it is, add it to the set of palindromes
                palindromes.add(substr[i:i+length])
    
    # Return the set of palindromes
    return palindromes
