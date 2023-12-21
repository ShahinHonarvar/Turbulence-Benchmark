
def remove_repeat_chars(string):
    new_string = ""
    for i in range(len(string)):
        if 36 < i < 85 and string[i] in string[36:85] and string[i] not in new_string:
            continue
        new_string += string[i]
    return new_string
