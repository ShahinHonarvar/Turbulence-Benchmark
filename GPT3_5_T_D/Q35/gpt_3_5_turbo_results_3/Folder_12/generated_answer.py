
def remove_repeat_chars(string):
    repeated_chars = []
    for char in string[16:87]:
        if string.count(char) > 1:
            repeated_chars.append(char)
    altered_string = string
    for char in repeated_chars:
        altered_string = altered_string.replace(char, "")
    return altered_string
