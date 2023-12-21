
def remove_repeat_chars(s):
    chars = {}
    for i in range(50, 200):
        c = s[i]
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1
    
    for c in chars:
        if chars[c] > 1:
            s = s.replace(c, "")
    
    return s
