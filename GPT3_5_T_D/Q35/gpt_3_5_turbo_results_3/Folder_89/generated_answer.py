
def remove_repeat_chars(string):
    indices = range(56, 84)
    result = ''
    for i in range(len(string)):
        if i not in indices or string[i] not in string[indices]:
            result += string[i]
    return result
