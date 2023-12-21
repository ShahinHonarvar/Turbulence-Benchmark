
def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()
    
    for i in range(1,8):
        for j in range(i, min(i+5, 8)):
            substring = string[i-1:j]
            if substring == substring[::-1] and len(substring) >= 3 and len(substring) <= 4:
                if substring.isalpha():
                    palindromes.add(substring)
    
    return palindromes
