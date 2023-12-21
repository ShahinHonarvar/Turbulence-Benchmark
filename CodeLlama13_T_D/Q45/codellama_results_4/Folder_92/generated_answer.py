
def palindromes_between_indices(string):
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over each possible arrangement of English letters in the string
    for i in range(4, 8):
        for j in range(i+1, 8):
            # Check if the substring between indices i and j is a palindrome
            substr = string[i:j]
            if substr == substr[::-1]:
                # Add the palindrome to the set
                palindromes.add(substr)
    
    return palindromes
