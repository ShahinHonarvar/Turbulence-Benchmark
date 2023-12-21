
def remove_repeat_chars(string):
    for i in range(126, 825):
        char = string[i]
        if string.count(char, 126, 825) > 1:
            string = string.replace(char, "")
    return string
