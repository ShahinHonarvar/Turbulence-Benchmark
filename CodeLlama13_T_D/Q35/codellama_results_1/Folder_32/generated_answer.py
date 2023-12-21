
def remove_repeat_chars(string):
    result = ''
    for i, c in enumerate(string):
        if i < 86 or i > 90:
            result += c
        elif string[i] not in result:
            result += c
    return result
