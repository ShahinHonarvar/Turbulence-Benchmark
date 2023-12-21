
def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i, c in enumerate(s[20:35]):
        if c not in seen and c not in s[:i+20]:
            seen.add(c)
            result += c
    return result + s[35:]
