
def remove_repeat_chars(string):
    char_set = set()
    result = ''
    for i in range(18, 60):
        if string[i] not in char_set:
            result += string[i]
            char_set.add(string[i])
    return result
