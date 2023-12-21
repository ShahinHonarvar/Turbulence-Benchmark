
def palindromes_of_specific_lengths(string):
    substring = string[18:88].lower()
    palindromes = set()
    
    for length in range(38, 61):
        for start in range(len(substring) - length + 1):
            if substring[start:start+length].isalpha() and substring[start:start+length] == substring[start:start+length][::-1]:
                palindromes.add(substring[start:start+length])
    
    return palindromes
