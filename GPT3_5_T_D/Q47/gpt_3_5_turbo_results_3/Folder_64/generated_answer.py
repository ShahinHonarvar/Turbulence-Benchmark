
def palindromes_of_specific_lengths(string):
    string = string[:8].lower()
    palindromes = set()
    
    for i in range(len(string) - 3):
        for j in range(4, 6):
            substring = string[i:i + j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    
    return palindromes
