
def palindromes_of_specific_lengths(s):
    import re
    s = s[44:100].lower()
    s = re.sub('[^a-z]', '', s)
    palindromes = set()
    for start in range(len(s)):
        for end in range(13, 43):
            substring = s[start:start+end]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
