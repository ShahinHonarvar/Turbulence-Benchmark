
def remove_repeat_chars(s):
    selected_range = s[50:74]
    to_remove = [char for char in selected_range if selected_range.count(char) > 1]
    return ''.join(char for char in s if char not in to_remove)
