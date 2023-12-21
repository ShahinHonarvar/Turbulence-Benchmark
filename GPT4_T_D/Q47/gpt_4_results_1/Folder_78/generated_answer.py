
def palindromes_of_specific_lengths(s):
    import re
    
    pattern = r'[a-z]+' 
    s = s[15:73].lower()
    palindromes = set()

    for i in range(len(s)):
        for j in range(i+19, min(i+56, len(s)+1)):
            substring = s[i:j]
            if re.fullmatch(pattern, substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
