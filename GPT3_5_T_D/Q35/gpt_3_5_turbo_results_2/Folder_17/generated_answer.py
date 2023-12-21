
def remove_repeat_chars(string):
    return string[:73] + ''.join([char for char in string[73:84] if string[73:84].count(char) == 1]) + string[84:]
