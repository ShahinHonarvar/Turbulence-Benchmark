
def remove_repeat_chars(string):
    substring = string[51:92]
    unique_chars = set(substring)
    for char in unique_chars:
        if substring.count(char) > 1:
            string = string.replace(char, '')
    return string
