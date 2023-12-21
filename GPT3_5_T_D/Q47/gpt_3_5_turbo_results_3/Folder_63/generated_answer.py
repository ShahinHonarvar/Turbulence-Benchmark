
def palindromes_of_specific_lengths(string):
    substring = string[33:86].lower()
    palindromes = set()
    
    for length in range(26, 32):
        for i in range(len(substring)-length+1):
            sub = substring[i:i+length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    
    return palindromes
