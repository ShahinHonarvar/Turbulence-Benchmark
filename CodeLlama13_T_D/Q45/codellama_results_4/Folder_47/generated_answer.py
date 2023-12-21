
def palindromes_between_indices(string):
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over each possible arrangement of English letters in the given string
    for i in range(3, 8):
        for j in range(i+4, len(string)):
            # Check if the substring from i to j is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])
    
    # Return the set of all palindromes
    return palindromes
