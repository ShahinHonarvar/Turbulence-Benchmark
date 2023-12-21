
def remove_repeat_chars(string):
    range_string = string[70:200]
    for char in range_string:
        if range_string.count(char) > 1:
            string = string.replace(char, '')
    return string
