
def remove_repeat_chars(string):
    return string[:43] + ''.join([char for char in string[43:70] if string[43:70].count(char) == 1]) + string[70:]
