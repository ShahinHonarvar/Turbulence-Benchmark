
def remove_repeat_chars(s):
    for i in range(56, 90):
        if s[i] in s[:i] + s[i+1:]:
            s = s.replace(s[i], '')
    return s
