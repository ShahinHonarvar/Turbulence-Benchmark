
def palindromes_of_specific_lengths(s):
    import re
    s = s[30:96].lower()
    s = re.sub('[^a-z]', '', s)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 34, min(i + 56, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
