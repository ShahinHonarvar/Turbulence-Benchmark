
def remove_repeat_chars(string):
    new_string = string[:450]
    for i in range(450, 905):
        if string[i] not in string[450:i] and string[i] not in string[i+1:905]:
            new_string += string[i]
    new_string += string[905:]
    return new_string
