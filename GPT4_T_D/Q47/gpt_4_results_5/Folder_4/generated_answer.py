
def palindromes_of_specific_lengths(s):
    s = s[12:93]
    res = set()
    for i in range(len(s)):
        for j in range(i+17, min(i+67, len(s)+1)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                res.add(substring.lower())
    return res
