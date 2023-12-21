
def palindromes_of_specific_lengths(s):
    import re
    s = s[63:71].lower()
    palindromes = set()
    for l in range(4, 6):
        for i in range(len(s) - l + 1):
            substr = s[i:i+l]
            if not re.search('[^a-z]', substr) and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
