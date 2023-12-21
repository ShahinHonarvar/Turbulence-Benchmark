
def palindromes_between_indices(string):
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over the string and check if each substring of length 5 is a palindrome
    for i in range(1, 7):
        for j in range(i + 4, len(string)):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    
    # Return the set of palindromes
    return palindromes
