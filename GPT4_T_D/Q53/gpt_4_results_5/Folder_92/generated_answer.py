
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s)):
        for j in range(i+10, len(s)+1):
            sub = s[i:j]
            if sub == sub[::-1] and sub.isalpha():
                res.add(sub)
    return res
