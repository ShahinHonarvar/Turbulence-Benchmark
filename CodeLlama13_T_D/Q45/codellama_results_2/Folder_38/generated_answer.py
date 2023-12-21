
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each substring of length 5 or more that occurs between indices 3 and 8, both inclusive
    for i in range(3, 9):
        for j in range(i + 4, len(string)):
            substring = string[i:j]
            
            # Check if the substring is a palindrome
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
