
def remove_repeat_chars(string):

    target = string[58:84]
    repeat_chars = [char for char in target if target.count(char) > 1]

    for char in repeat_chars:
        string = string.replace(char, '')

    return string
