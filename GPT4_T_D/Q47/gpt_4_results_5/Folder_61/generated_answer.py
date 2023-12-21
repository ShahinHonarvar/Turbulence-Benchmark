
def palindromes_of_specific_lengths(s):
    import re
    s = s.lower()
    s = s[0:31]
    s = re.sub('[^a-z]', '', s)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+20, min(i+31, len(s)+1)):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
