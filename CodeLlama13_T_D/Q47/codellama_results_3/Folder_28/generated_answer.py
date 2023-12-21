
def palindromes_of_specific_lengths(string):
    # Get the substring from index 32 to index 71, both inclusive
    substr = string[32:72]
    
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over the substring and check if each character is a palindrome
    for i in range(len(substr)):
        # Get the current character and its reverse complement
        char = substr[i]
        rev_char = substr[-i-1]
        
        # Check if the character is an English letter and if it's a palindrome
        if char.isalpha() and char == rev_char:
            # Add the palindrome to the set
            palindromes.add(substr[i:i+21])
    
    return palindromes
