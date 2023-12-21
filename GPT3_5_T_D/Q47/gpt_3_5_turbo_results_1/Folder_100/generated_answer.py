
def palindromes_of_specific_lengths(string):
    substr = string[29:97]
    palindromes = set()
    
    for length in range(12, 19):
        for i in range(len(substr) - length + 1):
            substring = substr[i:i+length].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    
    return palindromes
