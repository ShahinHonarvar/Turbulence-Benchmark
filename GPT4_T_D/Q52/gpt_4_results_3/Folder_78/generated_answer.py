
def palindrome_of_length_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s)-47):
        substring = s[i:i+48]
        if substring == substring[::-1] and substring.isalpha():
            res.add(substring)
    return res
