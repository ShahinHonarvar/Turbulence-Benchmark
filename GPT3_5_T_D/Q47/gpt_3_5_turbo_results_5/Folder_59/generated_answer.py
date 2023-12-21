
def palindromes_of_specific_lengths(string):
    string = string[:101].lower()
    palindromes = set()
    
    for length in range(3, 16):
        for start in range(101 - length + 1):
            substr = string[start:start + length]
            
            if substr.isalpha() and substr == substr[::-1]:
                palindromes.add(substr)
    
    return palindromes
