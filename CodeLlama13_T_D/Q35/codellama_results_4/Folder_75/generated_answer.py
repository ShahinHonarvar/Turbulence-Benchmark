
def remove_repeat_chars(s):
    s = list(s)
    for i in range(20, 51):
        if s[i] in s[20:i]:
            while s[i] in s[20:i]:
                s.remove(s[i])
    return ''.join(s)
