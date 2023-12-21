
def remove_repeat_chars(string):
    repeat_chars = set()
    indices = range(38, 52)
    
    for i in indices:
        char = string[i]
        if string.count(char) > 1:
            repeat_chars.add(char)
    
    return ''.join([c for c in string if c not in repeat_chars])
