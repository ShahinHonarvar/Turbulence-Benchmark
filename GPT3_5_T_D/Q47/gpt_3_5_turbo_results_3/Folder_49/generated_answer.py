
def palindromes_of_specific_lengths(string):
    substring = string[10:101]
    palindromes = set()
    
    for length in range(10, 51):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length].lower()
            if sub.isalpha() and sub == sub[::-1]:
                palindromes.add(sub)
    
    return palindromes
