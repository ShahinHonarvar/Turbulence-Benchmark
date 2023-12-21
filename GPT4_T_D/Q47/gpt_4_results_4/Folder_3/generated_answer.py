
def palindromes_of_specific_lengths(s):
    s = s[27:96].lower()
    res = set()
    for l in range(49, 52):
        for i in range(len(s)-l+1):
            substr = s[i:i+l]
            if substr == substr[::-1] and substr.isalpha():
                res.add(substr)
    return res
