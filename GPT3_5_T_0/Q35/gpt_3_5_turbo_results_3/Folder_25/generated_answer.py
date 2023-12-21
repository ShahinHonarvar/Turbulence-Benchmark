
def remove_repeat_chars(string):
    return string[:37] + ''.join([char for char in string[37:43] if string[37:43].count(char) == 1]) + string[43:]
