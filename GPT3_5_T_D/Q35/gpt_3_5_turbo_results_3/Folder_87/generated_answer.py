
def remove_repeat_chars(string):
    if len(string) >= 43:
        for i in range(21, 43):
            if string[i] in string[20:43] and string.count(string[i]) > 1:
                string = string.replace(string[i], '')
    return string
