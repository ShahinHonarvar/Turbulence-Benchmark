
def remove_repeat_chars(s):
    s = list(s)
    for i in range(20, 35):
        if s[i] in s[20:i]:
            s = [c for c in s if c != s[i]]
    return ''.join(s)
