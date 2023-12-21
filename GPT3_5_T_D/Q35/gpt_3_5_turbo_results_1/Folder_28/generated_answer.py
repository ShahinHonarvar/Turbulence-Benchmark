
def remove_repeat_chars(string):
    repeat_chars = set()
    for char in string[86:99]:
        if string[86:99].count(char) > 1:
            repeat_chars.add(char)
    altered_string = ''
    for char in string:
        if char in repeat_chars:
            continue
        altered_string += char
    return altered_string
