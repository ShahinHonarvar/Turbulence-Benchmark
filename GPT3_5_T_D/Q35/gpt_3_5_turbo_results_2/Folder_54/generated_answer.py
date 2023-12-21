
def remove_repeat_chars(string):
    return string[:35] + ''.join([char for char in string[35:64] if string[35:64].count(char) == 1]) + string[64:]
