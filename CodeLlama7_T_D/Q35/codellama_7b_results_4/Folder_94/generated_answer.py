
def remove_repeat_chars(s):
    for i in range(42, 87):
        c = s[i]
        while c in s and i + 1 < len(s) and s[i + 1] == c:
            s = s[:i] + s[i + 2:]
    return s
