
def remove_repeat_chars(string):
    for i in range(69, 97):
        char_count = string.count(string[i])
        if char_count > 1:
            string = string.replace(string[i], '')
    return string
