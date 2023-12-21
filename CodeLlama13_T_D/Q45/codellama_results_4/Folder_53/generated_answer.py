
def palindromes_between_indices(string):
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over each substring of length 6 between indices 4 and 8, both inclusive
    for i in range(4, 9):
        for j in range(i+5, len(string)):
            substring = string[i:j]
            
            # Check if the substring is a palindrome
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
