
def remove_repeat_chars(string):
    return string[:68] + ''.join(char for char in string[68:99] if string[68:99].count(char) == 1) + string[99:]
