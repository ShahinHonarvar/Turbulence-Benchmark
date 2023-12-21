
def remove_repeat_chars(string):
    if len(string) <= 70:
        return string
    else:
        return string[:13] + ''.join([ch for ch in string[13:70] if string[13:70].count(ch) == 1]) + string[70:]
