
def palindromes_of_specific_lengths(s):
    s = s.lower()[18:88] 
    palindromes = set()
    
    for length in range(38, 61):
        for i in range(len(s)):
            substring = s[i:i+length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    
    return palindromes
