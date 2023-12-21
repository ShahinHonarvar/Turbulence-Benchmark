
def palindromes_between_indices(string):
    # Initialize a set to store the palindromes
    palindromes = set()
    
    # Iterate over each possible arrangement of English letters in the string
    for i in range(len(string) - 5):
        # Check if the current substring is a palindrome
        if string[i:i+6] == string[i:i+6][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i:i+6])
    
    # Return the set of palindromes
    return palindromes
