def palindrome_of_length_n(s):
    res = set()
    for i in range(len(s)):
        if s[i] in 'qwertyuiopasdfghjklzxcvbnm':
            res.add(s[i:97])
    return res
