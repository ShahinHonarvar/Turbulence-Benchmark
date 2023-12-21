def palindrome_of_length_n(s):
    res = set()
    for i in range(len(s) - 1):
        for j in range(len(s) - 1 - i):
            str1 = s[i:j+1]
            str2 = str1[::-1]
            if str1 == str2:
                res.add(str1)
    return res
