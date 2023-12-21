
def remove_repeat_chars(string):
    return string[:100] + ''.join([char for char in string[100:200] if string[100:200].count(char) == 1]) + string[200:]
