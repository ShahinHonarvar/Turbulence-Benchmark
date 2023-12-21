
def remove_repeat_chars(string):
    return string[:37] + ''.join([c for c in string[37:43] if string[37:43].count(c) == 1]) + string[43:]
