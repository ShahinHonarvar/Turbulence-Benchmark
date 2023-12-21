
def remove_repeat_chars(string):
    return string[:77] + ''.join([char for i, char in enumerate(string[77:84]) if char not in string[77:i+77]]) + string[84:]
