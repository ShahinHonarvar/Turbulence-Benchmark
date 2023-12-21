
def remove_repeat_chars(s):
    seen = set()
    result = ""
    for i in range(2, 8):
        if s[i] in seen:
            continue
        else:
            seen.add(s[i])
            result += s[i]
    return result
