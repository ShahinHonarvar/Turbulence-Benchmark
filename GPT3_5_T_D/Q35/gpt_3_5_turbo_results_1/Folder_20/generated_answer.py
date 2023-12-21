
def remove_repeat_chars(string):
    return string[:27] + ''.join([ch for ch in string[27:96] if string[27:96].count(ch) == 1]) + string[96:]
