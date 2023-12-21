
def palindrome_of_length_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s)):
        if i + 116 > len(s):
            break
        substring = s[i:i+116]
        if substring == substring[::-1] and substring.isalpha():
            res.add(substring)
    return res
