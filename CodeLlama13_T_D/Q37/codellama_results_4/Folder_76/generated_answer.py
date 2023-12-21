
def filter_chars(s):
    res = ""
    for i in range(len(s)):
        if s[i].isalnum() and 379 <= i <= 898:
            if 'M' <= s[i] <= 'v':
                continue
        res += s[i]
    return res
