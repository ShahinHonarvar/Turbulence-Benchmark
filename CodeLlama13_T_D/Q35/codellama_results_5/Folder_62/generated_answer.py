
def remove_repeat_chars(s):
    seen = {}
    for i in range(50, 92):
        if s[i] in seen:
            s = s[:i] + s[i+1:]
    return s
