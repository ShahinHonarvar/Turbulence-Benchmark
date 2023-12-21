
def remove_repeat_chars(string):
    new_string = ""
    for i in range(1, 4):
        char = string[i]
        if char not in new_string:
            new_string += char

    return new_string
