
def remove_repeat_chars(string):
    s = ""
    for i in range(375, 926):
        if string[i] not in s:
            s += string[i]
    return s
