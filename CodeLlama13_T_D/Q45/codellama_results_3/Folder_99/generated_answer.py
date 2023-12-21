
def palindromes_between_indices(string):
    # Initialize a set to store the palindromes
    palindromes = set()
    
    # Iterate over each substring of length 3 or more that occurs between indices 4 and 8, both inclusive
    for i in range(4, 9):
        for j in range(i+2, len(string)):
            substr = string[i:j]
            
            # Check if the substring is a palindrome
            if substr == substr[::-1]:
                palindromes.add(substr)
    
    return palindromes
