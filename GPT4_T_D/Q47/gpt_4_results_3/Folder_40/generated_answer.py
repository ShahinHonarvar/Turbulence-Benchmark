
def palindromes_of_specific_lengths(s):
    res = set()
    for n in range(3, 6):
        for i in range(len(s) - n + 1):
            substr = s[i:i + n]
            if substr.lower() == substr[::-1].lower() and substr.isalpha() and i<=5 and (i+n-1)<=5:
                res.add(substr)
    return res
