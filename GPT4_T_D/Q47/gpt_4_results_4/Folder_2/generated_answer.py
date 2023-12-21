
def palindromes_of_specific_lengths(s):
    import re
    s = s[10:60]
    s = re.sub('[^a-z]+', '', s.lower())
    palindromes = set()
    for length in range(18, 37):
        for i in range(len(s) - length + 1):
            substr = s[i:i+length]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
