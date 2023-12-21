
def remove_repeat_chars(string):
    return string[:77] + ''.join([char for char in string[77:84] if string[77:84].count(char) == 1]) + string[84:]
