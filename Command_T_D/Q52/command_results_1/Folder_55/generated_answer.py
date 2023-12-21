def palindrome_of_length_n(s):
    res = set()
    for i in range(len(s) - 97):
        j = i + 97
        if s[i:j].lower() == s[j:i].lower():
            res.add(s[i:j])
    return res
