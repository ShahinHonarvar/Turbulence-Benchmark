
def remove_repeat_chars(string):
    seen = set()
    result = ''
    for char in string[86:90]:
        if char not in seen:
            seen.add(char)
            result += char
    return result + string[90:]
