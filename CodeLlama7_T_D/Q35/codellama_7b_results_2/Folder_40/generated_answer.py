 def remove_repeat_chars(s):
    res = ""
    for i in range(len(s)):
        if s[i] not in res:
            res += s[i]
    return res
