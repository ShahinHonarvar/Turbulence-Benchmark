
def palindromes_of_specific_lengths(s):
    import re
    s = s[15:73]
    res = set()
    for length in range(19, 56):
        for i in range(len(s) - length + 1):
            substr = s[i : i + length]
            if substr == substr[::-1] and re.match('^[a-zA-Z]*$', substr):
                res.add(substr.lower())
    return res
