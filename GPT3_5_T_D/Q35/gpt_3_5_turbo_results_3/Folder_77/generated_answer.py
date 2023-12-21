

def remove_repeat_chars(string):
    return string[:355] + ''.join([char for char in string[355:988] if string[355:988].count(char) == 1]) + string[988:]
