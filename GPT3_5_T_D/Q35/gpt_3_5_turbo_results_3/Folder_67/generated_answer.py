
def remove_repeat_chars(string):
    repeated_chars = set()
    for i in range(45, 67):
        char = string[i]
        if string.count(char, 45, 67) > 1:
            repeated_chars.add(char)
    altered_string = ''
    for char in string:
        if char not in repeated_chars or string.index(char) < 44 or string.index(char) >= 67:
            altered_string += char
    return altered_string
