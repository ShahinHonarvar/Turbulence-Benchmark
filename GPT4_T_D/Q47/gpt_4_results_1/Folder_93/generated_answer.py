
def palindromes_of_specific_lengths(s):
    import re
    s = s[17:96]
    s = re.sub('[^a-zA-Z]', '', s.lower())
    palindromes = set()
    for i in range(96-17+1):
        for j in range(i+13, min(i+50, 96-17+1)):
            substr = s[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
