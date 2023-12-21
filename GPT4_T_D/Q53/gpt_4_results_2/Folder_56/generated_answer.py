
def palindrome_of_length_at_least_n(s):
    import re
    s = re.sub(r'\W+', '', s).lower()
    res = set()
    for i in range(len(s)):
        for j in range(i+84, len(s)+1):
            if s[i:j]==s[i:j][::-1]:
                res.add(s[i:j])
    return res
