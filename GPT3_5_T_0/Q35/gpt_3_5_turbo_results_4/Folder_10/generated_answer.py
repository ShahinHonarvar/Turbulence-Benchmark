
def remove_repeat_chars(string):
    return string[:36] + ''.join([char for char in string[36:54] if string[36:54].count(char) == 1]) + string[54:]
