
def palindrome_of_length_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s)):
        for j in range(i+21, len(s)+1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                res.add(substring)
    return res
