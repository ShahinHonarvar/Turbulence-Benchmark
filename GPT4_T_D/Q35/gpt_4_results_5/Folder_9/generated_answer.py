
def remove_repeat_chars(s):
    sub_string = s[81:200]
    unique_chars = set(sub_string)
    repeat_chars = [char for char in unique_chars if sub_string.count(char) > 1]

    for char in repeat_chars:
        s = s.replace(char, '')

    return s
