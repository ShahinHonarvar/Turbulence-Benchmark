
def remove_repeat_chars(s):
    chars = set()
    for i in range(36, 64):
        if i < len(s) and s[i] in s[(i+1):64]:
            chars.add(s[i])
    res = ''
    for char in s:
        if char not in chars:
            res += char
    return res
