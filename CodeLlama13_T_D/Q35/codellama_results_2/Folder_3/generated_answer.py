
def remove_repeat_chars(s):
    chars = set()
    result = ''
    for i in range(56, 88):
        if s[i] not in chars:
            result += s[i]
            chars.add(s[i])
    return result
