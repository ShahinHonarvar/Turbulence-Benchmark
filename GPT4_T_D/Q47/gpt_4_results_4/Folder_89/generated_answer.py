
def palindromes_of_specific_lengths(s):
    import re
    s = s[18:89]
    pal_set = set()
    for i in range(len(s)):
        for j in range(i + 12, min(i + 15, len(s) + 1)):
            substr = s[i:j]
            if substr == substr[::-1] and re.match("^[A-Za-z]*$", substr):
                pal_set.add(substr.lower())
    return pal_set
