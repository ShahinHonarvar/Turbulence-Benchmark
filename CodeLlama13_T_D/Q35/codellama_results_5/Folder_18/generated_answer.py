
def remove_repeat_chars(string):
    s = ''
    for i in range(56, 90):
        if string[i] not in s:
            s += string[i]
    return ''.join(s)
