
def palindromes_of_specific_lengths(string):
    substring = string[30:85]
    substring = substring.lower()
    palindromes = set()
    
    for length in range(12, 21):
        for i in range(len(substring) - length + 1):
            if substring[i:i+length] == substring[i:i+length][::-1] and substring[i:i+length].isalpha():
                palindromes.add(substring[i:i+length])
    
    return palindromes
