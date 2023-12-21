
def remove_repeat_chars(string):
    unique_chars = set(string[:8])
    result = ''
    for char in string:
        if char not in unique_chars:
            result += char
    return result
