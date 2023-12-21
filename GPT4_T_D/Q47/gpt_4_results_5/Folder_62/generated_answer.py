
def palindromes_of_specific_lengths(s):
    import re
    s = s[26:88]
    palindromes = set()
    for i in range(52, 57):
        for j in range(len(s) - i + 1):
            segment = re.sub('[^a-z]', '', s[j:j+i].lower())
            if len(segment) != i:
                continue
            if segment == segment[::-1]:
                palindromes.add(segment)
    return palindromes
