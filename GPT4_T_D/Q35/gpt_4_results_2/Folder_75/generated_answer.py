
def remove_repeat_chars(s):
    unique_chars = set(s[21:51])
    for char in unique_chars:
        if s[21:51].count(char) > 1:
            s = s.replace(char, "")
    return s
