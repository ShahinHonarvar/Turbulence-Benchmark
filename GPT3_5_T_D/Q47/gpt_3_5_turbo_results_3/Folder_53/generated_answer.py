
def palindromes_of_specific_lengths(string):
    string = string[1:300].lower()
    palindromes = set()
    
    for length in range(3, 11):
        for start in range(len(string) - length + 1):
            substring = string[start:start+length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
