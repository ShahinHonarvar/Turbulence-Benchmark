
def remove_repeat_chars(string):
    for i in range(30, 200):
        char = string[i]
        if char in string[i + 1:200]:
            string = string.replace(char, '')
    return string
