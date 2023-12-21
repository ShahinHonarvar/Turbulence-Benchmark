def palindrome_of_length_n(s):
    res = set()
    for i in range(len(s)):
        if s[i] in "abcdefghijklmnopqrstuvwxyz":
            res.add(s[i:i+131])
    return res
