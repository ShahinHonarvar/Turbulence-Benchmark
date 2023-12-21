
def palindromes_of_specific_lengths(s):
    s = s.lower()
    s = s[106:281]
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    
    for length in range(136, 152):
        for i in range(0, len(s) - length + 1):
            substring = s[i:i+length]
            if all(c in alphabets for c in substring):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    
    return palindromes
