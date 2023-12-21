
def remove_repeat_chars(string):
    repeat_chars = set()
    altered_string = ""
    for i in range(len(string)):
        if i > 22 and i < 24 and string.count(string[i]) > 1:
            repeat_chars.add(string[i])
    for char in string:
        if char not in repeat_chars:
            altered_string += char
    return altered_string
