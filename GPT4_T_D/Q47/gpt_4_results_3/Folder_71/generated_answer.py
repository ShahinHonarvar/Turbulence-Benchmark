
def palindromes_of_specific_lengths(s):
    import re
    s = s[18:66]
    s = re.sub('[^a-zA-Z]', '', s)
    s = s.lower()
    palindromes = set()
    for length in range(23, 37):
        for i in range(0, len(s) - length + 1):
            substring = s[i: i+length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
