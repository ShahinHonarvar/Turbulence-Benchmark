
def palindromes_of_specific_lengths(s):
    import re
    s = s[30:85]
    res = set()
    for l in range(12, 21):
        for i in range(0, len(s) - l + 1):
            substr = s[i:i+l]
            if substr.lower() == substr[::-1].lower() and re.match("^[a-z]*$", substr.lower()):
                res.add(substr)
    return res
