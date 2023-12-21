
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over the string and check if each substring of length 4 is a palindrome
    for i in range(len(string) - 3):
        substr = string[i:i+4]
        if substr == substr[::-1]:
            palindromes.add(substr)
    
    # Return the set of palindromes
    return palindromes
