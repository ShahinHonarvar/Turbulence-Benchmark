
def remove_repeat_chars(string):
    new_string = string[:1]
    for char in string[1:8]:
        if string[1:8].count(char) == 1:
            new_string += char
    new_string += string[8:]
    return new_string
