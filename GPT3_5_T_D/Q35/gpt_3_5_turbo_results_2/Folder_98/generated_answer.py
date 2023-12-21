
def remove_repeat_chars(string):
    for i in range(7):
        char = string[i]
        if string.count(char) > 1:
            string = string.replace(char, "")
            string = string[:i] + char + string[i:]
    return string
