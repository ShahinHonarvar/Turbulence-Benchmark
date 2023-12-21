
def palindromes_between_indices(string):
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over each substring of length 7 in the string
    for i in range(1, len(string) - 6):
        # Check if the substring is a palindrome
        if string[i:i+7] == string[i:i+7][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i:i+7])
    
    # Return the set of palindromes
    return palindromes
