
def palindromes_of_specific_lengths(string):
    substring = string[22:96]
    palindromes = set()
    
    for length in range(52, 56):
        for start in range(len(substring) - length + 1):
            sub = substring[start:start+length].lower()
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
                
    return palindromes
