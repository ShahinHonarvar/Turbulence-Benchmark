
def remove_repeat_chars(string):
    return string[:36] + ''.join([char for char in string[36:85] if string[36:85].count(char) == 1]) + string[85:]
