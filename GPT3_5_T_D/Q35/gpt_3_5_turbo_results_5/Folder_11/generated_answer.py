
def remove_repeat_chars(s):
    unique_chars = set(s[48:76])
    for char in unique_chars:
        if s[48:76].count(char) > 1:
            s = s.replace(char, "")
    return s
