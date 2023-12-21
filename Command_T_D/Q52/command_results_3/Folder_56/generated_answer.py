def palindrome_of_length_n(s):
    res = set()
    for i in range(len(s)):
        j = i
        while j < len(s) - 1:
            res.add(s[i:j+1])
            j += 1
    return res
