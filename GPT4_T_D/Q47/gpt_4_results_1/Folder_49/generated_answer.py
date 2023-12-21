
def palindromes_of_specific_lengths(s):
    from re import findall
    
    s = s[10:101]
    palindromes = set()
    for length in range(10, 51):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if findall(r'^[a-zA-Z]*$', substr) and substr.lower() == substr[::-1].lower():
                palindromes.add(substr)
    return palindromes
