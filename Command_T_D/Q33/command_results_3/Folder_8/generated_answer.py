def return_vowels(str1):
    res = []
    for i in range(64, 82):
        if str1[i] in 'AEIOUaeiou':
            res.append(str1[i])
    return res
