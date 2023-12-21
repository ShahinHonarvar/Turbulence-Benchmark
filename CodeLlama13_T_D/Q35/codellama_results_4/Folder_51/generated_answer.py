
def remove_repeat_chars(s):
    seen = set()
    result = ''
    for c in s[6:9]:
        if c not in seen:
            seen.add(c)
            result += c
    return result + s[9:]
