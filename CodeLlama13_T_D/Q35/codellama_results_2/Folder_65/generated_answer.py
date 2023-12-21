
def remove_repeat_chars(string):
    chars = set()
    result = ''
    for i in range(51, 76):
        if string[i] not in chars:
            chars.add(string[i])
            result += string[i]
    return result
