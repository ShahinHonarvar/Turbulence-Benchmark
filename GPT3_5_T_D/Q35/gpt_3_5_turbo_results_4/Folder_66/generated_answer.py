
def remove_repeat_chars(string):
    new_string = ""
    for i in range(len(string)):
        if 11 < i < 76 and string.count(string[i]) > 1:
            continue
        new_string += string[i]
    return new_string
