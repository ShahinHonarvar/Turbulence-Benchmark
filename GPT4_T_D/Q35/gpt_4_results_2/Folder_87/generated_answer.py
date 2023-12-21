
def remove_repeat_chars(s):
    unique_chars = set(s[21:43])
    repeat_chars = [char for char in unique_chars if s[21:43].count(char) > 1]
    for char in repeat_chars:
        s = s.replace(char, '')
    return s
