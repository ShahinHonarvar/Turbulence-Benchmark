
def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i, c in enumerate(s[3:8]):
        if i not in seen and s.count(c) == 1:
            result += c
            seen.add(i)
    return result + s[8:]
