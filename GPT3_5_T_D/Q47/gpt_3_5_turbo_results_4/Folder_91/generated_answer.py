
def palindromes_of_specific_lengths(string):
    string = string[:11].lower()
    palindromes = set()
    
    for length in range(3, 6):
        for i in range(len(string) - length + 1):
            substring = string[i:i+length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
