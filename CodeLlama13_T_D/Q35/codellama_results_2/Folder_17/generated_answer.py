
def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i, char in enumerate(s[73:84], 73):
        if char not in seen and i < len(s) - 1 and s[i + 1] == char:
            continue
        result += char
        seen.add(char)
    return result
