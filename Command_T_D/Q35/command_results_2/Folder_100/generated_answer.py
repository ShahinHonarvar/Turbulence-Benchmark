def remove_repeat_chars(s):
    for i in range(len(s)-1):
        if s[i] in s[i+1:]:
            s = s[:i] + s[i+1:]
    return s
