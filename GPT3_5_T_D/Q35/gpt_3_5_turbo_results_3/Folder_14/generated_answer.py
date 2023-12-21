
def remove_repeat_chars(string):
    new_string = string[:2]
    for i in range(2, 5):
        if string[i] not in new_string:
            new_string += string[i]
    new_string += string[5:]
    return new_string
