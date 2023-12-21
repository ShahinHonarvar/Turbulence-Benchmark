
def remove_repeat_chars(string):
    return string[:70] + ''.join([char for char in string[70:200] if string[70:200].count(char) == 1]) + string[200:]
