
def remove_repeat_chars(string):
    return string[:18] + ''.join([char for char in string[18:60] if string[18:60].count(char) == 1]) + string[60:]
