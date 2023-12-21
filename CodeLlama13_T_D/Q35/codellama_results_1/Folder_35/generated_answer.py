
def remove_repeat_chars(s):
    chars = {}
    for i in range(77, 84):
        if s[i] in chars:
            chars[s[i]] += 1
        else:
            chars[s[i]] = 1
    
    for char in chars:
        while chars[char] > 1:
            s = s.replace(char, "")
            chars[char] -= 1
    
    return s
