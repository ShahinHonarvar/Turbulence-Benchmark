
def palindromes_of_specific_lengths(s):
    s = s[15:90] 
    palindromes = set()
    
    for i in range(len(s)):
        for j in range(i+40, min(i+72+1, len(s)+1)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
                
    return palindromes
