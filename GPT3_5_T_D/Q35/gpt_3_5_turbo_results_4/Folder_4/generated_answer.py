
def remove_repeat_chars(string):
    unique_chars = {}
    for i in range(49, 74):
        char = string[i]
        if char not in unique_chars:
            unique_chars[char] = True
        else:
            string = string.replace(char, '')
    return string
