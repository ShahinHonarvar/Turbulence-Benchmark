
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[27:78].lower()
    
    for i in range(len(substring) - 18):
        if substring[i:i+19] == substring[i:i+19][::-1]:
            palindromes.add(substring[i:i+19])
    
    return palindromes
