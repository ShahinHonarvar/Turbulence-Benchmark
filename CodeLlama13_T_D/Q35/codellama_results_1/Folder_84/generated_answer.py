
def remove_repeat_chars(string):
    chars = {}
    for i in range(32, 44):
        if string[i] in chars:
            del chars[string[i]]
        else:
            chars[string[i]] = True
    
    return ''.join([chars.get(c, c) for c in string])
