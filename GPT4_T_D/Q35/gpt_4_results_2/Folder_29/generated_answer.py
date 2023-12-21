
def remove_repeat_chars(s):
    unique_chars = set(s[71:98])
    duplicate_chars = [char for char in unique_chars if s[71:98].count(char) > 1]
    for char in duplicate_chars:
        s = s.replace(char, '')
    return s
