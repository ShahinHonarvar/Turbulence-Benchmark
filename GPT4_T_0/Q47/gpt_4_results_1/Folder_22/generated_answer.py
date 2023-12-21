
def palindromes_of_specific_lengths(s):
    import re
    s = s[100:201].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+5, min(i+11, len(s)+1)):
            substring = s[i:j]
            if substring == substring[::-1] and re.match("^[a-z]*$", substring):
                palindromes.add(substring)
    return palindromes
