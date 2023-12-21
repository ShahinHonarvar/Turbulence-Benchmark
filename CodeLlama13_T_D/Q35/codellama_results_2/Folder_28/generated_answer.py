
def remove_repeat_chars(string):
    new_str = ""
    for i in range(len(string)):
        if string[i] not in new_str or (i < 86 or i > 99):
            new_str += string[i]
    return new_str
