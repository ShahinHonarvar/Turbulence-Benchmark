
def palindromes_between_indices(string):
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over the string and check if each substring of length 4 or more is a palindrome
    for i in range(5, len(string) - 4):
        substring = string[i:i+4]
        if substring == substring[::-1]:
            palindromes.add(substring)
    
    # Return the set of palindromes
    return palindromes
