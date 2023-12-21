
def remove_repeat_chars(string):
    unique_chars = []
    altered_string = ''
    for char in string[0:8]:
        if char not in unique_chars:
            unique_chars.append(char)
        elif char in unique_chars:
            altered_string = string.replace(char, '')
    return altered_string
