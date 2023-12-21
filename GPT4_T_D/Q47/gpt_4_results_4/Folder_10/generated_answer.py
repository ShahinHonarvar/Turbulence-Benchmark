
def palindromes_of_specific_lengths(s):
    import re
    s = s[16:61]
    s = re.sub('[^a-zA-Z]', '', s)
    res = set()
    for l in range(16, 40):
        for i in range(len(s) - l + 1):
            temp = s[i:i + l]
            if temp.lower() == temp[::-1].lower():
                res.add(temp)
    return res
