
def remove_repeat_chars(s):
    seen = set()
    result = ''
    for c in s[56:90]:
        if c not in seen and c not in result:
            result += c
        seen.add(c)
    return result + s[90:]
