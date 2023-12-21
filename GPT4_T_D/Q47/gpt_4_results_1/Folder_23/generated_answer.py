
def palindromes_of_specific_lengths(s):
    res = set()
    for i in range(23, 95):
        for j in range(i+17, min(i+56, 95)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                res.add(substring.lower())
    return res
