
def remove_repeat_chars(string):
    return string[:57] + ''.join([char for char in string[57:85] if string[57:85].count(char) <= 1]) + string[85:]
