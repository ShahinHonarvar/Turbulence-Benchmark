
def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(37, min(85, len(s))):
        if s[i] in s[37:i] or s[i] in s[i+1:86]:
            repeat_chars.add(s[i])
    return ''.join(c for c in s if c not in repeat_chars)
