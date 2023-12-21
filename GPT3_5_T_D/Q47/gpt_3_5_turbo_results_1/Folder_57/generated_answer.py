
def palindromes_of_specific_lengths(string):
    substring = string[16:95]
    palindromes = set()
    
    for length in range(39, 53):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i+length].lower()
            
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    
    return palindromes
