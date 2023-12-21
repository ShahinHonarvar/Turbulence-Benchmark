
def remove_repeat_chars(string):
    sub_string = string[463:995]
    for char in sub_string:
        if sub_string.count(char) > 1:
            string = string.replace(char,'')
    return string
