
def remove_repeat_chars(string):
    new_string = ""
    for i in range(40, 200):
        if i < len(string) and string[i] not in string[40:i]:
            new_string += string[i]
    return new_string
