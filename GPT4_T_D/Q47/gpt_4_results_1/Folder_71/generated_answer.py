
def palindromes_of_specific_lengths(s: str):
    import re
    s = s.lower()
    s = s[18:66]
    s = re.sub(r'[^a-z]', '', s)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+23,i+37):
            substring = s[i:j]
            if len(substring) < 23 or len(substring) > 36:
                continue
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
