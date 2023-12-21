
def remove_repeat_chars(string):
    chars = {}
    for i in range(20, 43):
        char = string[i]
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
            string = string.replace(char, '')
    return string
