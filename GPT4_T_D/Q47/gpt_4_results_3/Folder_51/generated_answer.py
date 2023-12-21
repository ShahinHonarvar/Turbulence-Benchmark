
def palindromes_of_specific_lengths(s):
    s = s[2:9].lower()
    res = set()
    for i in range(len(s)):
        for j in range(3, 5):
            if i + j > len(s):
                continue
            sub = s[i:i+j]
            if sub == sub[::-1] and sub.isalpha():
                res.add(sub)
    return res
