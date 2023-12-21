
def palindromes_of_specific_lengths(s):
    import re
    s = s.lower()
    s = s[100:301]
    s = re.sub('[^a-z]', '', s)
    n = len(s)
    palindromes = set()

    for l in range(50, 101):
        for i in range(n-l+1):
            substring = s[i:i+l]
            if substring == substring[::-1]:
                palindromes.add(substring)

    return palindromes
