
def remove_repeat_chars(string):
    repeat_chars = set()
    for char in string[90:97]:
        if string.count(char) > 1:
            repeat_chars.add(char)
    new_string = ""
    for char in string:
        if char not in repeat_chars:
            new_string += char
    return new_string
