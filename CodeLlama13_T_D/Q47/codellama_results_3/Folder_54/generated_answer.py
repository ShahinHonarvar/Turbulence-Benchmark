
def palindromes_of_specific_lengths(string):
    # Find the substring from index 27 to index 77
    substr = string[27:78]
    
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each character in the substring
    for i in range(len(substr)):
        # Check if the current character is a palindrome of length 18 or 19
        if substr[i] in 'abcdefghijklmnopqrstuvwxyz' and len(substr[i]) in [18, 19]:
            # Add the current character to the set of palindromes
            palindromes.add(substr[i])
    
    # Return the set of palindromes
    return palindromes
