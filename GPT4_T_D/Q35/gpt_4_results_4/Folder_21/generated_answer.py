
def remove_repeat_chars(string):
    substring = string[463:995]
    repeat_chars = set([char for char in substring if substring.count(char) > 1])
    for char in repeat_chars:
        string = string.replace(char, '')
    return string
