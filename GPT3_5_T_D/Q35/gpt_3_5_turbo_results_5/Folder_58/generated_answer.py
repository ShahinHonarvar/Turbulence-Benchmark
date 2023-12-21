
def remove_repeat_chars(string):
    return string[:103] + ''.join([char for char in string[103:802] if string[103:802].count(char) == 1]) + string[802:]
