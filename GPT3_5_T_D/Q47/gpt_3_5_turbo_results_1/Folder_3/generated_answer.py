
def palindromes_of_specific_lengths(string):
    substr = string[27:96].lower()
    palindromes = set()
    
    for length in range(49, 52):
        for i in range(len(substr) - length + 1):
            substring = substr[i:i+length]
            
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    
    return palindromes
