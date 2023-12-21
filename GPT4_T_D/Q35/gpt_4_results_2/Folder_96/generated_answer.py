
def remove_repeat_chars(s):
    unique_chars = set()
    repeat_chars = set()
    for i in range(61, min(200, len(s))):
        if s[i] in unique_chars:
            repeat_chars.add(s[i])
        else:
            unique_chars.add(s[i])
    result = ''
    for c in s:
        if c not in repeat_chars:
            result += c
    return result
