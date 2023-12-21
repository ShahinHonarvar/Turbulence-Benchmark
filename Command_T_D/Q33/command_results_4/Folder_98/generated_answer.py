def return_vowels(str1):
    res = []
    for c in str1[3:9]:
        if c in "AEIOU" and c > "S" and c < "U":
            res.append(c)
    return res
