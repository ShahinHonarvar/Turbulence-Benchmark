
def palindromes_of_specific_lengths(s):
    import re
    s = s[35:89]
    s = re.sub('[^a-zA-Z]', '', s)
    s = s.lower()
    palindromes = set()
    for i in range(24, 34):
        for j in range(len(s)):
            if s[j:j+i] == s[j:j+i][::-1]:
                palindromes.add(s[j:j+i])
    return palindromes
