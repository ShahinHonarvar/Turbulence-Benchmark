
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s)):
        for j in range(i + 7, len(s)+1):
            sub_s = s[i: j]
            if sub_s == sub_s[::-1] and sub_s.isalpha():
                res.add(sub_s)
    return res
