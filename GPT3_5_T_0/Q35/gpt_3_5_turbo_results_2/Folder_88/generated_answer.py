
def remove_repeat_chars(string):
    return string[:3] + ''.join([char for char in string[3:9] if string[3:9].count(char) == 1]) + string[9:]
