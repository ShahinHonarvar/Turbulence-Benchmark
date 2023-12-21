
def remove_repeat_chars(string):
    for i in range(13, 70):
        if string[i - 1] == string[i]:
            string = string[:i - 1] + string[i:]
    return string
