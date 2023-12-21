
def palindromes_between_indices(string):
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over each possible arrangement of English letters in the given string between indices 1 and 8, both inclusive
    for i in range(1, 9):
        for j in range(i+3, len(string)):
            # Check if the substring from index i to index j is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])
    
    # Return the set of palindromes
    return palindromes
