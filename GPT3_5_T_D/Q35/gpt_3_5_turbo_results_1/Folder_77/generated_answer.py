
def remove_repeat_chars(string):
    return string[:355] + ''.join(c for c in string[355:988] if string[355:988].count(c) == 1) + string[988:]
