
def remove_repeat_chars(s):
    between_indices_chars = s[3:5]
    repeat_chars = [char for char in between_indices_chars if between_indices_chars.count(char) > 1]
    for char in set(repeat_chars):
        s = s.replace(char, '')
    return s
