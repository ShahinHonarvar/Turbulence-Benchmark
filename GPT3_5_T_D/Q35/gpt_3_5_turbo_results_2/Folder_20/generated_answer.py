
def remove_repeat_chars(string):
    indices_27_96 = string[27:96]
    for char in indices_27_96:
        if indices_27_96.count(char) > 1:
            string = string.replace(char, '')
    return string
