
def remove_repeat_chars(string):
    return string[:36] + ''.join([char for i, char in enumerate(string[36:85]) if string[36:85].count(char) == 1]) + string[85:]
