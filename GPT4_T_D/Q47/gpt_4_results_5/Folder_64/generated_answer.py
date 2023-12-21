
def palindromes_of_specific_lengths(s):
    import re
    s = s[:8].lower()
    results = set()
    for i in range(len(s)):
        for j in range(i+4, min(i+6, len(s)+1)):
            substring = s[i:j]
            if re.match('^[a-z]+$', substring) and substring == substring[::-1]:
                results.add(substring)
    return results
