
def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i in range(57, 84):
        if s[i] not in seen:
            result += s[i]
            seen.add(s[i])
    return result
