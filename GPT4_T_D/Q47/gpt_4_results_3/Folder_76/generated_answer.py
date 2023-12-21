
def palindromes_of_specific_lengths(s):
    import re
    s = s[101:293]
    s = re.sub('[^A-Za-z]', '', s)
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 154, min(i + 183, len(s) + 1)):
            segment = s[i:j]
            if segment == segment[::-1]:
                palindromes.add(segment)
    return palindromes
