def return_vowels(s):
    res = []
    for i in range(77, 84):
        if chr(i) in s:
            res.append(chr(i))
    return res
