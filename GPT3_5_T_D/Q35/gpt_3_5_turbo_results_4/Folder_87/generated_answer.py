
def remove_repeat_chars(string):
    return string[:20] + ''.join(char for char in string[20:43] if string[20:43].count(char) == 1) + string[43:]
