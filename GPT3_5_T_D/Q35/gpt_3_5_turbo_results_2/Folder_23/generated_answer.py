
def remove_repeat_chars(string):
    substring = string[20:36]
    for char in set(substring):
        if substring.count(char) > 1:
            string = string.replace(char, '')
    return string
