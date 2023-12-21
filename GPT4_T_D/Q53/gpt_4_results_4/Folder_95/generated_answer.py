
def palindrome_of_length_at_least_n(s):
    s = ''.join(ch for ch in s if ch.isalpha()).lower()
    length = len(s)
    res = set()
    for l in range(35, length+1):
        for i in range(length+1-l):
            sub = s[i:i+l]
            if sub == sub[::-1]:
                res.add(sub)
    return res
