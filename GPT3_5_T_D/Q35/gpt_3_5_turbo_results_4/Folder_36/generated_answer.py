
def remove_repeat_chars(string):
    new_string = string[:476]
    repeat_chars = set(string[476:709])
    for char in string[476:709]:
        if char not in repeat_chars:
            new_string += char
    new_string += string[709:]
    return new_string
