
def palindromes_of_specific_lengths(string):
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over the string and check if each substring is a palindrome
    for i in range(0, 21):
        for j in range(i + 5, min(i + 81, len(string))):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    
    # Return the set of palindromes
    return palindromes
