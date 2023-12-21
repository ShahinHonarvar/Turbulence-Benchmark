
def remove_repeat_chars(string):
    chars = {}
    for i in range(37, 43):
        if string[i] in chars:
            chars[string[i]] += 1
        else:
            chars[string[i]] = 0
    
    for char in chars:
        if chars[char] > 1:
            string = string.replace(char, '')
    
    return string
