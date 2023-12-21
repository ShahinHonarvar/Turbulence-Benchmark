
def remove_repeat_chars(s):
    selected = s[63:96]
    for char in selected:
        if selected.count(char) > 1:
            s = s.replace(char, '')
    return s
