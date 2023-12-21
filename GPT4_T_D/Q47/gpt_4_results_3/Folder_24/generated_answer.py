
def palindromes_of_specific_lengths(s):
    s = s[12:93]  
    res = set()

    for l in range(42, 78):
        for i in range(len(s)):
            if i + l > len(s):
                break
            substr = s[i:i + l]
            if substr == substr[::-1] and substr.isalpha():
                res.add(substr.lower())

    return res
