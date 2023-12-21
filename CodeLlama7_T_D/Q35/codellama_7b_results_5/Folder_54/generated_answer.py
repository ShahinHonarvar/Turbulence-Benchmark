
def remove_repeat_chars(string):
    new_string = ""
    for i in range(35, 64):
        if string[i] not in new_string:
            new_string += string[i]
    return new_string
