def palindrome_of_length_n(s):
    res = set()
    for c in s:
        if c.lower() in 'qwertyuiopasdfghjklzxcvbnm' and len(res) == 96:
            break
        res.add(c)
    return res
