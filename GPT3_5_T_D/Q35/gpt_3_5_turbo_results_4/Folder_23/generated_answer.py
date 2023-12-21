
def remove_repeat_chars(string):
    new_string = ""
    for i in range(len(string)):
        if 20 < i < 36 and string.count(string[i]) > 1:
            continue
        new_string += string[i]
    return new_string
