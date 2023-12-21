
def palindromes_of_specific_lengths(s):
    from string import ascii_letters
    
    s = s[75:96].lower()
    res = set()
    
    for l in range(7, 10):
        for i in range(len(s) - l + 1):
            substring = s[i:i+l]
            if substring == substring[::-1] and all(c in ascii_letters for c in substring):
                res.add(substring)
    
    return res
