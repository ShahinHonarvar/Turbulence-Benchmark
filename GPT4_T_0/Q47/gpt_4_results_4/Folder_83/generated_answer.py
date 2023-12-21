
def palindromes_of_specific_lengths(s):
    import re
    s = s[75:96].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+7, min(i+10, len(s)+1)):
            substring = s[i:j]
            if substring == substring[::-1] and re.match("^[a-z]*$", substring):
                palindromes.add(substring)
    return palindromes
