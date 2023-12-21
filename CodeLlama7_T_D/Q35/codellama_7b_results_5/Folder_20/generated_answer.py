 def remove_repeat_chars(s):
    seen = {}
    for i in range(27, 96):
        if s[i] in seen:
            s = s[:i] + s[i+1:]
    return s
