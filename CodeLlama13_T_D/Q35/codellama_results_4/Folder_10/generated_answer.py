
def remove_repeat_chars(s):
    chars = {}
    for i, c in enumerate(s[36:54]):
        if c not in chars:
            chars[c] = 0
        chars[c] += 1
    
    new_str = ''
    for i, c in enumerate(s):
        if i >= 36 and i < 54:
            if chars[c]:
                new_str += c
                chars[c] -= 1
            else:
                new_str += ' '
        else:
            new_str += c
    return new_str
