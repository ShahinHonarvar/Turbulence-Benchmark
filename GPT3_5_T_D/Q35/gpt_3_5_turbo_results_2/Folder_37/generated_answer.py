
def remove_repeat_chars(string):
    return string[:2] + ''.join(char for char in string[2:7] if string[2:7].count(char) < 2) + string[7:]
