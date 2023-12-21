
def palindromes_of_specific_lengths(string):
    palindromes = set()
    
    for i in range(13, 99 + 1):
        for j in range(i, 99 + 1):
            substr = string[i:j]
            
            if len(substr) >= 26 and len(substr) <= 29 and substr == substr[::-1]:
                palindromes.add(substr)
    
    return palindromes
