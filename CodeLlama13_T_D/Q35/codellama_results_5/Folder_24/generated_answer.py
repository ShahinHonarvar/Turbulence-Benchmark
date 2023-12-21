
def remove_repeat_chars(s):
    seen = set()
    result = ''
    for c in s[13:91]:
        if c not in seen and c not in result:
            result += c
        seen.add(c)
    return result + s[91:]
