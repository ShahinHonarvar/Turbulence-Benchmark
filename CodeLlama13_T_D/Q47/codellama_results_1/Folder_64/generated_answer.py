
def palindromes_of_specific_lengths(string):
    # Set of palindromes
    palindromes = set()
    
    # Loop through each substring of length 4 to 5
    for i in range(4, 6):
        for j in range(len(string) - i + 1):
            substr = string[j:j+i]
            if substr == substr[::-1]:
                palindromes.add(substr)
    
    return palindromes
