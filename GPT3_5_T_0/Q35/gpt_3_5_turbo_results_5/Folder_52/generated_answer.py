
def remove_repeat_chars(string):
    return string[:38] + ''.join([char for char in string[38:81] if string[38:81].count(char) == 1]) + string[81:]
