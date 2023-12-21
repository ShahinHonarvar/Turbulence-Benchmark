
def remove_repeat_chars(s):
    seen = set()
    new_str = ''
    for i in range(10, 80):
        if s[i] not in seen:
            new_str += s[i]
            seen.add(s[i])
    return new_str
