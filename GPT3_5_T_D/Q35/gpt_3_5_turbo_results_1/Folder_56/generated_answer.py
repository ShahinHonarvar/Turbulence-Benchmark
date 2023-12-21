
def remove_repeat_chars(string):
    return string[:7] + ''.join([char for char in string[7:9] if string[7:9].count(char) == 1]) + string[9:]
