
def remove_repeat_chars(string):
    string = string[:29] + ''.join([char for char in string[29:53] if string[29:53].count(char) <= 1]) + string[53:]
    return string
