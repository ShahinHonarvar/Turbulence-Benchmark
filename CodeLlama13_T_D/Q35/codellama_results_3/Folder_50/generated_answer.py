
def remove_repeat_chars(string):
    new_str = ''
    for i in range(13, 76):
        if string[i] not in new_str:
            new_str += string[i]
    return new_str
