
def remove_repeat_chars(string):
    new_string = ''
    for i in range(18, 60):
        if string[i] in string[i+1:60]:
            string = string[:i] + string[i+1:].replace(string[i], '')
    return string
