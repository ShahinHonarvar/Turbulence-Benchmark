
def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i, c in enumerate(s[18:60], 18):
        if c not in seen and i != len(s) - 1:
            result += c
            seen.add(c)
    return result + s[len(s) - 1]
