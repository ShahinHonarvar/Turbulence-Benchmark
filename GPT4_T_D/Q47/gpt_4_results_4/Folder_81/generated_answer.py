
def palindromes_of_specific_lengths(s):
    from string import ascii_letters
    ADJUSTED_LENGTH = min(len(s), 122+1)       
    s = s[12:ADJUSTED_LENGTH]
    palindromes = set()
    for l in range(12, 221):
        for i in range(len(s) - l + 1):
            sub_s = s[i:i+l]
            if sub_s == sub_s[::-1] and sub_s.lower() == sub_s.lower()[::-1] and set(sub_s).issubset(ascii_letters):
                palindromes.add(sub_s)
    return palindromes
