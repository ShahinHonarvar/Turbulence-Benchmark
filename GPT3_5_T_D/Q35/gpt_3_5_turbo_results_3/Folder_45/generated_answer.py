
def remove_repeat_chars(string):
    return string[:40] + ''.join([char for char in string[40:200] if string[40:200].count(char) == 1]) + string[200:]
