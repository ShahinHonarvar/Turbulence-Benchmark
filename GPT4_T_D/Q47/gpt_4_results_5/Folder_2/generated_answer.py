
def palindromes_of_specific_lengths(s):
    import re
    s = s[10:60]
    s = re.sub(r'[^a-z]', '', s.lower())
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+18, i+37):
            if j <= len(s):
                substr = s[i:j]
                if substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes
