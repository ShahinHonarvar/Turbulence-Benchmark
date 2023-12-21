
def remove_repeat_chars(string):
    new_string = string[:3]
    for i in range(3,8):
        if string[i] not in string[:i] + string[i+1:]:
            new_string += string[i]
    new_string += string[8:]
    return new_string
