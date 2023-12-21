
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each possible arrangement of English letters in the given string
    for i in range(4, 10):
        for j in range(i+1, 10):
            # Check if the current substring is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])
    
    # Return the set of palindromes
    return palindromes
