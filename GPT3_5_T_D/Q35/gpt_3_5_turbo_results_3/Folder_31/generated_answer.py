
def remove_repeat_chars(string):
    unique_chars = set()
    for i in range(33, 78):
        char = string[i]
        if char in unique_chars:
            string = string.replace(char, '')
        else:
            unique_chars.add(char)
    return string
