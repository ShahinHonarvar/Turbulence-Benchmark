
def remove_repeat_chars(string):
    return string[:200] + ''.join(char for i, char in enumerate(string[200:202]) if string[200:202].count(char) == 1) + string[202:]
