
def remove_repeat_chars(s):
    seen = set()
    result = ""
    for c in s:
        if 73 <= ord(c) < 84 and c not in seen:
            seen.add(c)
            result += c
    return result
