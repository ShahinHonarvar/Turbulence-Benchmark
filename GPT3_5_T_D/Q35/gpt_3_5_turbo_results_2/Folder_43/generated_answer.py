
def remove_repeat_chars(string):
    new_string = string[:10]
    for char in string[10:28]:
        if string.count(char) == 1:
            new_string += char
    new_string += string[28:]
    return new_string
