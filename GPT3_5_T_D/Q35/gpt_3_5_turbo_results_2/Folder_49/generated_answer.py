
def remove_repeat_chars(string):
    return string[:90] + ''.join([char for char in string[90:200] if string[90:200].count(char) == 1]) + string[200:]
