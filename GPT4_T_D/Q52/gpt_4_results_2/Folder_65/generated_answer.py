
def palindrome_of_length_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if len(substring) == 35 and substring == substring[::-1] and substring.isalpha():
                res.add(substring)
    return res
