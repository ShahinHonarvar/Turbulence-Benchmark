
def remove_repeat_chars(string):
    return string[:450] + ''.join([char for char in string[450:905] if string[450:905].count(char) == 1]) + string[905:]
