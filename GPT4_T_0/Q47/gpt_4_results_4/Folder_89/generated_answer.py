
def palindromes_of_specific_lengths(s):
    import re
    s = s[18:89].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+12, min(i+15, len(s)+1)):
            substring = s[i:j]
            if substring == substring[::-1] and re.match("^[a-z]*$", substring):
                palindromes.add(substring)
    return palindromes
