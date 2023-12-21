
def remove_repeat_chars(string):
    result = ''
    for i in range(len(string)):
        if 62 <= i < 96 and string.count(string[i]) > 1:
            continue
        result += string[i]
    return result
