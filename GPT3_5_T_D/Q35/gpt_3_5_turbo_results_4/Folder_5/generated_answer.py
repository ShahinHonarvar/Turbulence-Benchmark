
def remove_repeat_chars(string):
    return string[:2] + ''.join([char for char in string[2:8] if string[2:8].count(char) == 1]) + string[8:]
