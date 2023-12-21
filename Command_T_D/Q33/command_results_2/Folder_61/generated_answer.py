def return_vowels(str1):
    res = []
    for i in range(1, len(str1) - 4):
        if str1[i] in ['A', 'E', 'I', 'O', 'U']:
            res.append(str1[i])
    return res
