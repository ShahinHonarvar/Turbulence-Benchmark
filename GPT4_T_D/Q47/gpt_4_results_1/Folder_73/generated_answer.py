
def palindromes_of_specific_lengths(s):
    s = s[21:63].lower()
    res = set()
    for i in range(len(s)):
        for j in range(i+22, min(i+34, len(s)+1)):
            sub = s[i:j]
            if sub == sub[::-1] and sub.isalpha():
                res.add(sub)
    return res
