 
def remove_repeat_chars(string):
    new_string = string[0:16]
    for i in range(16, 87):
        if string[i] in string[16:i] or string[i] in string[i+1:87]:
            continue
        else:
            new_string += string[i]
    new_string += string[87:]
    return new_string
