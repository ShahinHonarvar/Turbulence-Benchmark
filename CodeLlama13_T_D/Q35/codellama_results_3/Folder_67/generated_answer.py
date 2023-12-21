
def remove_repeat_chars(string):
    seen = set()
    result = ''
    for char in string[44:67]:
        if char not in seen and char != '':
            seen.add(char)
            result += char
    return result
