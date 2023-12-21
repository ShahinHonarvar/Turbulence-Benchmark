
def palindromes_of_specific_lengths(s):
    import re
    s = s[75:96].lower()
    res = set()
    for i in range(len(s)):
        for j in range(i+7, min(i+10, len(s)+1)):
            sub_str = s[i:j]
            if sub_str == sub_str[::-1] and re.match("^[a-z]*$", sub_str):
                res.add(sub_str)
    return res
