
def palindromes_of_specific_lengths(s):
    allowed_characters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s = s[34:91]
    palindromes = set()
    
    for length in range(14, 40):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if set(substring).issubset(allowed_characters) and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    
    return palindromes
