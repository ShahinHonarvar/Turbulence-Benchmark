
def remove_repeat_chars(string):
    return string[:45] + ''.join([char for char in string[45:48] if string[45:48].count(char) == 1]) + string[48:]
