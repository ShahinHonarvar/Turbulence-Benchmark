
def palindromes_of_specific_lengths(s):
    s = s[43:96].lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s = ''.join(ch for ch in s if ch in alphabet)
    
    palindromes = set()
    
    for i in range(len(s)):
        for j in reversed(range(i+17, min(i+48, len(s)+1))):
            substr = s[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
                break
    return palindromes
