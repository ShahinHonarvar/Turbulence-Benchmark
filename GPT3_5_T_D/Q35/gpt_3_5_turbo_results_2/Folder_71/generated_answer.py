
def remove_repeat_chars(string):
    return string[:20] + ''.join(ch for ch in string[20:35] if string[20:35].count(ch) == 1) + string[35:]
