
def remove_repeat_chars(s):
    selected_chars = s[73:93]
    to_remove = [char for char in selected_chars if selected_chars.count(char) > 1]
    for char in to_remove:
        s = s.replace(char, '')
    return s
