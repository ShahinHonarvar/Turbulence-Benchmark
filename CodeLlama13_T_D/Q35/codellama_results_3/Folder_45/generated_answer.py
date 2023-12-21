
def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i, char in enumerate(s):
        if i < 40 or i > 200:
            continue
        if char not in seen:
            seen.add(char)
            result += char
    return result
