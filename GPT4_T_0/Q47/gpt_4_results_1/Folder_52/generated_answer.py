
def palindromes_of_specific_lengths(s):
    import re
    s = s[44:100]
    s = re.sub('[^a-zA-Z]', '', s)
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+13, min(i+43, len(s)+1)):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
