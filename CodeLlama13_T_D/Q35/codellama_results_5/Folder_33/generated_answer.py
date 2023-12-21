
def remove_repeat_chars(s):
    chars = set()
    result = ""
    for i in range(125, 825):
        if s[i] not in chars:
            result += s[i]
            chars.add(s[i])
    return result
