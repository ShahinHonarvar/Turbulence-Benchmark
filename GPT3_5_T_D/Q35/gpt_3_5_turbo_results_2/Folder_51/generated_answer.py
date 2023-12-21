
def remove_repeat_chars(string):
    new_string = string[:6]
    repeated_chars = set(string[6:9])
    for char in string[9:]:
        if char not in repeated_chars:
            new_string += char
    return new_string
