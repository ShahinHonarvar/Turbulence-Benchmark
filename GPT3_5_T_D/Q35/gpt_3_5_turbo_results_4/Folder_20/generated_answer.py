
def remove_repeat_chars(string):
    new_string = ""
    for i in range(len(string)):
        if i < 27 or i >= 96 or string[i] not in string[27:96]:
            new_string += string[i]
    return new_string
